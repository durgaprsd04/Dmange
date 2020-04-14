from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Course, Facutly
# Create your views here.
from django.http import HttpResponse


def index(request):
    list_of_courses = Course.objects.all()
    context = {'list_of_courses':list_of_courses}  
    template = loader.get_template('dmange_app/index.html')
    return HttpResponse(template.render(context, request))

def create_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    faculties = Facutly.objects.all()
    context ={'course':course, 'list_of_faculties':faculties}
    template = loader.get_template('dmange_app/create_course.html')
    return HttpResponse(template.render(context, request))

def finish_course(request):
    return HttpResponse("Done creating course for the year")
