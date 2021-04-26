from django.http import HttpResponse, HttpRequest
from django.template import loader

from .models import Post

# Create your views here.
def index(request: HttpRequest):
    return HttpResponse('OK')

def post_list(request: HttpRequest):
    posts = Post.objects.order_by('id')
    template = loader.get_template('blog/posts.html')
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

def post_detail(request: HttpRequest, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponse('Post does not exist!', status=404)
    template = loader.get_template('blog/post.html')
    context = { 'post': post }
    return HttpResponse(template.render(context, request))