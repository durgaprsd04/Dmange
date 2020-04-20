from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Course, Facutly, CourseForYear, CourseRegistrationForYear, Student
import datetime
# Create your views here.
from django.http import HttpResponse

class UserAction:
    def __init__(self, action, action_name):
        self.action_href = action
        self.action_name = action_name

class PendingApprovalCourseDetails:
    def __init__(self,course_id,  student_id, student_name, course_code, course_name):
        self.course_id = course_id
        self.student_id = student_id
        self.student_name = student_name
        self.course_code = course_code
        self.course_name = course_name

def index(request):
    list_of_courses = Course.objects.all()
    list_of_courses_for_year = CourseForYear.objects.filter(year__year = datetime.datetime.now().year)
    username = request.user.username
    
    user_type = 'Faculty' if 'F' in username else 'Student'
    if user_type == 'Faculty' :
        list_of_courses = list_of_courses
        list_of_user_actions = [
            UserAction('#','Create new course1'),
            UserAction('#','Create new course for year'),
            UserAction('approve_course', 'Approve registered students')]
    else:
        list_of_courses = list_of_courses_for_year
        list_of_user_actions = ['Register for course']


    context = {'list_of_courses':list_of_courses,
    'user_type':user_type,
    'username':username,
    'list_of_user_actions':list_of_user_actions}  
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
    course_for_year = CourseForYear.objects.create(course_code=course, faculty_id=faculty_id, year=academic_year)
    course_for_year.save()
    context={'course_name':course.course_name, 'year':academic_year,'faculty_name':faculty_name,'faculty_id':faculty_id}
    template = loader.get_template("dmange_app/finish_course.html")
    return HttpResponse(template.render(context, request))

def course_registration(request, course_code):
    course_for_year = CourseForYear.objects.get(id=course_code)
    course = Course.objects.get(id = course_for_year.course_code_id)
    faculty = Facutly.objects.get(faculty_id=course_for_year.faculty_id)
    year = course_for_year.year.year
    context ={'faculty':faculty,'course':course,'year':year , 'course_for_year_id':
    course_code}
    template = loader.get_template("dmange_app/course_registration.html")
    return HttpResponse(template.render(context, request))

def finish_course_registration(request):
    course_id = request.POST['course_for_year_id']
    course_for_year = CourseForYear.objects.get(id=course_id)
    user_name = request.user.username
    course_reg_for_year = CourseRegistrationForYear.objects.create(course_for_year_id = course_for_year, student_id = user_name, approved=False)
    course_reg_for_year.save()
    return HttpResponse("registered successfully")

def approve_course(request):
    user_name = request.user.username
    if 'F' in user_name:
        list_of_courses_pending_approval =[]
        student_details ={}
        courses_list = CourseForYear.objects.filter(faculty_id = user_name)
        reg_courses_list = CourseRegistrationForYear.objects.filter(approved = False)
        for course in courses_list:
            for reg_course in reg_courses_list:
                if(course.course_code.course_code == reg_course.course_for_year_id.course_code.course_code):
                    student_name = Student.objects.get(student_id = reg_course.student_id).student_name
                    course_code = reg_course.course_for_year_id.course_code.course_code
                    course_name = reg_course.course_for_year_id.course_code.course_name
                    pending_course = PendingApprovalCourseDetails(reg_course.id, reg_course.student_id, student_name, course_code, course_name )
                    list_of_courses_pending_approval.append(pending_course)

    context={'list_of_courses_pending_approval':list_of_courses_pending_approval, 'student_details':student_details}
    template = loader.get_template("dmange_app/pending_approval.html")
    return HttpResponse(template.render(context, request))
            

def approve_courses(request):
    list_of_approved_courses= []
    for key in request.POST.keys():
        if 'course_reg_' in key:
            list_of_approved_courses.append(request.POST[key])
    for course_id in list_of_approved_courses:
        course = CourseRegistrationForYear.objects.get(id=course_id)
        course.approved = True
        course.save()
    return HttpResponse('Course approved')