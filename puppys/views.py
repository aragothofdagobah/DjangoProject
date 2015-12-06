from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('puppys/index.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('puppys/Contact.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('puppys/About.html')
    return HttpResponse(template.render())


def shihTzu(request):
    template = loader.get_template('puppys/shihTzu.html')
    return HttpResponse(template.render())


def toyPoodle(request):
    template = loader.get_template('puppys/toyPoodle.html')
    return HttpResponse(template.render())
