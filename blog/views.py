from django.http import HttpResponse, HttpRequest
from django.template import loader

from .models import Post

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('blog/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def about(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('blog/about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.order_by('id')
    template = loader.get_template('blog/posts.html')
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponse('Post does not exist!', status=404)
    template = loader.get_template('blog/post.html')
    context = { 'post': post }
    return HttpResponse(template.render(context, request))