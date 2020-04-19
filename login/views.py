from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template import RequestContext

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
        return redirect('/dmange_app/', context_instance=RequestContext(request))
    else:
        return HttpResponse('no user')


def logout_user(request):
    logout(request)
    return HttpResponse('logged out successfully')

def change_password(request):
    pass
