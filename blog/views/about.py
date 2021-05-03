from django.http import HttpResponse, HttpRequest
from django.template import loader

def get_about_page(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('blog/about.html')
    context = {}
    return HttpResponse(template.render(context, request))