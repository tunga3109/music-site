from django.urls import path
from .views import main, post_detail, contact, posts

urlpatterns = [
    path('', main, name='blog_main'),
    path('posts/', posts, name='blog_posts'),
    # path('contact/', contact, name='blog_contact'),
    # # path('about/', about, name='blog_about'),
    # path('<slug:post_slug>/', post_detail, name='blog_post')
]