from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    template = loader.get_template("login/login_page.html")
    context ={'test':'wonderman'}
    return HttpResponse(template.render(context, request))

def login_user(request):
    username = request.POST['userName']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request,user)
        return HttpResponse('user exists')
    else:
        return HttpResponse('no user')


def logout(request):
    pass

def change_password(request):
    pass
