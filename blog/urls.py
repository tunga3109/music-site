from django.urls import path
from .views import main, posts, about, contact, post_detail

urlpatterns = [
    path('', main, name='blog_main'),
    path('posts/', posts, name='blog_posts'),
    path('about/', about, name='blog_about'),
    path('contact/', contact, name='blog_contact'),
    path('<slug:post_slug>/', post_detail, name='blog_post')

]