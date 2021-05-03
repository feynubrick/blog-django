from django.http import HttpResponse, HttpRequest
from django.template import loader

from blog.models import Post

def get_post_list_page(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.order_by('id')
    template = loader.get_template('blog/posts.html')
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

def get_post_detail_page(request: HttpRequest, post_id: int) -> HttpResponse:
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponse('Post does not exist!', status=404)
    template = loader.get_template('blog/post.html')
    context = { 'post': post }
    return HttpResponse(template.render(context, request))