from django.urls import path
from .views import MainListView, AboutTemplateView, PostListView, PostDetailView, ContactCreateView

urlpatterns = [
    path('', MainListView.as_view(), name='blog_main'),
    path('posts/', PostListView.as_view(), name='blog_posts'),
    path('about/', AboutTemplateView.as_view(), name='blog_about'),
    path('contact/', ContactCreateView.as_view(), name='blog_contact'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='blog_post')

]