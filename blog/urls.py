from django.urls import path

from .views import home, about, post_list, post_detail

urlpatterns = [
    path('', home, name='blog_home'),
    path('about', about, name='blog_about'),
    path('posts', post_list, name='blog_posts'),
    path('posts/<int:post_id>', post_detail, name='blog_post'),
]