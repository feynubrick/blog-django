from django.http import HttpResponse, HttpRequest

from .models import Post

# Create your views here.
def index(request: HttpRequest):
    return HttpResponse('OK')

def post_list(request: HttpRequest):
    post_queryset = Post.objects.order_by('id')
    titles = [str(post) for post in post_queryset]
    title_list_text = ','.join(titles)
    return HttpResponse(title_list_text)

def post_detail(request: HttpRequest, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponse('Post does not exist!', status=404)
    
    return HttpResponse(str(post))