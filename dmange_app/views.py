from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Course, Facutly, CourseForYear
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
    course_code = request.POST['course_code']
    course = get_object_or_404(Course, course_code=course_code)
    faculty_id = request.POST['faculty_id']
    faculty_name = Facutly.objects.get(faculty_id=faculty_id).faculty_name
    academic_year = request.POST['academic_year']
    #course_for_year = CourseForYear.objects.create(course_code=course, faculty_id=faculty_id, year=academic_year)
    #course_for_year.save()
    context={'course_name':course.course_name, 'year':academic_year,'faculty_name':faculty_name,'faculty_id':faculty_id}
    template = loader.get_template("dmange_app/finish_course.html")
    return HttpResponse(template.render(context, request))