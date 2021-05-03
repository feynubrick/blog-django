from django.urls import path

from blog.views.home import get_home_page
from blog.views.about import get_about_page
from blog.views.posts import get_post_list_page, get_post_detail_page

urlpatterns = [
    path('', get_home_page, name='blog_home'),
    path('about', get_about_page, name='blog_about'),
    path('posts', get_post_list_page, name='blog_posts'),
    path('posts/<int:post_id>', get_post_detail_page, name='blog_post'),
]