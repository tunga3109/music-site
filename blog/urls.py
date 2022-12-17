from django.urls import path
from .views import main, posts, about, contact

urlpatterns = [
    path('', main, name='blog_main'),
    path('posts/', posts, name='blog_posts'),
    path('about/', about, name='blog_about'),
    path('contact/', contact, name='blog_contact'),
]