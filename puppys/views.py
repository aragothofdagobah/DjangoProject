from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import ToyPoodle, ShihTzu


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
    puppy_list = ShihTzu.objects.order_by('-Name')
    template = loader.get_template('puppys/shihTzu.html')
    context = RequestContext(request, {
        'puppy_list': puppy_list,
    })
    return HttpResponse(template.render(context))


def toyPoodle(request):
    puppy_list = ToyPoodle.objects.order_by('-Name')
    template = loader.get_template('puppys/toyPoodle.html')
    context = RequestContext(request, {
        'puppy_list': puppy_list,
    })
    return HttpResponse(template.render(context))
