from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .models import Post, Contact
from .forms import ContactForm


class BaseMixin:
    context = {
        'twitter': 'https://twitter.com',
        'facebook': 'https://facebook.com',
        'linkedin': 'https://linkedin.com',
        'instagram': 'https://instagram.com',
    }


class MainListView(BaseMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'MUZLOVE'
        context['phone_number'] = '+375336377999'
        context['email_address'] = 'tunga3109@gmail.com'
        context['form'] = ContactForm()
        context.update(self.context)
        return context

    def post(self, request: HttpRequest):
        if request.POST.get('form_type') == 'contact_form':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
        return self.get(request=request)


class AboutTemplateView(BaseMixin, TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['heading'] = 'ABOUT US'
        context['about'] = '''
                It is a long established fact that a reader will be distracted by the 
                readable content of a page when looking at its layout.
                The point of using Lorem
        '''
        return context


class PostListView(BaseMixin, ListView):
    template_name = "blog/posts_list.html"
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'Latest posts'
        context.update(self.context)
        return context


class PostDetailView(BaseMixin, DetailView):
    template_name = 'blog/posts.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context


class ContactCreateView(BaseMixin, CreateView):
    template_name = 'blog/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('blog_posts')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['heading'] = 'Contact'
        return context

# def post_detail(request: HttpRequest, post_slug: str):
#     post = get_object_or_404(Post, slug=post_slug)
#     return render(request, 'blog/posts.html', {'post': post})


# def contact(request: HttpRequest):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = ContactForm()
#     return render(request, 'blog/contact.html', {'contact_form': form})


# def posts(request: HttpRequest):
#     posts = Post.objects.all()
#     return render(request, 'blog/posts_list.html', {'posts': posts})  # !!!!!!!! переделать


def error404(request, exception):
    return render(request, 'blog/error_404.html')



