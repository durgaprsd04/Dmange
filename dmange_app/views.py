from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {}
    template = loader.get_template('dmange_app/index.html')
    return HttpResponse(template.render(context, request))
