from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.views.decorators.http import require_GET

from .models import Post
from .forms import ContactForm


@require_GET
def main(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {'posts': posts})


def post_detail(request: HttpRequest, post_slug: str):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, 'blog/post.html', {'post': post})


def contact(request: HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'blog/contact.html', {'contact_form': form})


def posts(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})  # !!!!!!!! переделать


def error404(request, exception):
    return render(request, 'blog/error_404.html')


def about(request: HttpRequest):
    return render(request, 'blog/about.html')
