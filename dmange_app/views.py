from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Course, Facutly, CourseForYear, CourseRegistrationForYear
import datetime
# Create your views here.
from django.http import HttpResponse


def index(request):
    list_of_courses = Course.objects.all()
    list_of_courses_for_year = CourseForYear.objects.filter(year__year = datetime.datetime.now().year)
    context = {'list_of_courses':list_of_courses,'list_of_courses_for_year':list_of_courses_for_year}  
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

def course_registration(request, course_code):
    course_for_year = CourseForYear.objects.get(id=course_code)
    course = Course.objects.get(id = course_for_year.course_code_id)
    faculty = Facutly.objects.get(faculty_id=course_for_year.faculty_id)
    context ={'faculty':faculty,'course':course}
    template = loader.get_template("dmange_app/course_registration.html")
    return HttpResponse(template.render(context, request))


