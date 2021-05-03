from django.http import HttpResponse, HttpRequest
from django.template import loader

def get_home_page(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('blog/home.html')
    context = {}
    return HttpResponse(template.render(context, request))