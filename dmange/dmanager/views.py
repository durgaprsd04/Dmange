from django.shortcuts import render
from .models import student,courses,department,reg_course, reg_student, faculty, staff, programappings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import StudentForm, DepartmentForm, CourseForm, LoginForm, FacultyForm, StaffForm
import time
from django.db.models import Max
from django.contrib.auth.models import User
import re
import json

# Create your views here.
##adding stuff to the DB. Currently called only by staff
def put_student(request):
    if(request.method=='POST'):
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        # process the data in form.cleaned_data as required
        # redirect to a new URL:
            name = form.cleaned_data['name']
            program = form.cleaned_data['program']
            specialization = form.cleaned_data['specialization']
            departmentname = form.cleaned_data['department']
            idfrom =str(student.objects.all().aggregate(Max('id'))['id__max']+1+1000)
            year=time.asctime( time.localtime(time.time()) ).split(' ')[4]
            rollnumber=program+year[-2:]+idfrom[1:5]+departmentname[0:2]
            studentsadded=0
            try:
                student.objects.create(rollnumber=rollnumber, name=name, program=program,specialization=specialization,department_id=department.objects.get(departmentcode=departmentname).id )
                User.objects.create_user(rollnumber, '',rollnumber)
                studentsadded=1
            except Exception as e:
                studentsadded=0
            return render(request, 'homeviews/staff_home.html',{'studentsadded':studentsadded,'username':request.user.first_name})
        # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()
        return render(request, 'homeviews/partials/staff_student_input_form.htm', {'form': form.as_p()})

def put_department(request):
    if(request.method=='POST'):
        form = DepartmentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            departmentname = form.cleaned_data['departmentname']
            hodname = form.cleaned_data['hodname']
            departmentcode = form.cleaned_data['departmentcode']
            departmentsadded=0
            try:
                department.objects.create(departmentname=departmentname,hod=hodname,departmentcode=departmentcode)
                departmentsadded=1
            except Exception as e:
                departmentsadded=0
            return render(request, 'homeviews/staff_home.html',{'departmentsadded':departmentsadded,'username':request.user.first_name})    
        # if a GET (or any other method) we'll create a blank form
    else:
        form = DepartmentForm()
        return render(request, 'homeviews/partials/staff_department_input_form.htm', {'form': form.as_p()})

    
#Changing put course to add faculty also.
def put_course(request):
    if(request.method=='POST'):
        form = CourseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            input_name = form.cleaned_data['name']
            input_program = form.cleaned_data['program']
            departmentcode = form.cleaned_data['department']
            idfrom =str(courses.objects.all().aggregate(Max('id'))['id__max']+1+1000)
            coursecode=departmentcode[:2]+input_program+idfrom
            dpcourse=department.objects.get(departmentcode=departmentcode)
            coursesadded=0
            try:
                dpcourse.courses_set.create(coursecode=coursecode,name=input_name, program=input_program)
                coursesadded = 1
            except Exception as e:
                coursesadded =0
            if('staff' in request.user.username):
                return render(request, 'homeviews/staff_home.html',{'coursesadded':coursesadded,'username':request.user.first_name})
            elif('fac' in request.user.username):
                return render(request, 'homeviews/faculty_home.html',{'coursesadded':coursesadded,'username':request.user.first_name})
        # if a GET (or any other method) we'll create a blank form
    else:
        form = CourseForm()
        if('staff' in request.user.username):
            return render(request, 'homeviews/partials/staff_course_input_form.htm', {'form': form.as_p()})
        elif('fac' in request.user.username):
            return render(request, 'homeviews/partials/staff_course_input_form.htm', {'form': form.as_p()})
def put_faculty(request):
    if(request.method =='POST'):
        form = FacultyForm(request.POST)
        if(form.is_valid()):
            name = form.cleaned_data["facultyname"]
            departmentcode = form.cleaned_data["department"]
            isperm = form.cleaned_data["isperm"]
            username = form.cleaned_data["username"]
            dpfaculty=department.objects.get(departmentcode=departmentcode)
            facultyadded=0
            try:
                dpfaculty.faculty_set.create(facultyname=name, isperm=isperm, username=username)
                User.objects.create_user('fac_'+username+str(faculty.objects.get(username=username).id), '',username+str(faculty.objects.get(username=username).id))
                facultyadded=1
            except Exception as e:
                facultyadded=0
            return render(request, 'homeviews/staff_home.html',{'facultyadded':facultyadded,'username':request.user.first_name})
    else:
        form = FacultyForm()
        return render(request, 'homeviews/partials/staff_faculty_input_form.htm', {'form': form.as_p()})

def put_staff(request):
    if(request.method=='POST'):
        form = StaffForm(request.POST)
        if(form.is_valid()):
            staffname = form.cleaned_data["staffname"]
            departmentcode = form.cleaned_data["department"]
            staffusername = form.cleaned_data["staffusername"]
            dpstaff = department.objects.get(departmentcode=departmentcode)
            staffadded=0
            try:
                dpstaff.staff_set.create(staffname=staffname, username = staffusername)
                user = User.objects.create_user('staff_'+staffusername+str(staff.objects.get(username=staffusername).id), '',staffusername+str(staff.objects.get(username=staffusername).id))
                staffadded=1
            except Exception as e:
                staffadded=0
            return render(request, 'homeviews/staff_home.html',{'staffadded':staffadded,'username':request.user.first_name})
    else:
        form = StaffForm()
        return render(request,'homeviews/partials/staff_staff_input_form.htm', {'form': form.as_p()})

    
# add more delete permissions and extend the class
def staff_faculty_delete(request):
    facultyid = request.GET['id']
    fd = faculty.objects.get(id=int(facultyid))
    fd.delete()
    return render(request, 'homeviews/staff_home.html',{'facultydeleted':1,'facultyid':facultyid })
###    

##Listing courses for view in general, might be removed later on.
def  list_courses(request):
    if(request.method=='POST'):
        listofcourses=courses.objects.all()
        return render(request, 'homeviews/student_home.html',{'listofcourses':listofcourses})
    else:
        listofcourses=[]
        return render(request, 'homeviews/student_home.html',
                     {'courselist':listofcourses})

def  faculty_course_partial_view(request):
    listofregcourses = reg_course.objects.values('courseid_id')
    lreg=[]
    for j in listofregcourses:
        lreg.append(j['courseid_id'])
    lcourse=[]
    listofcourse = courses.objects.values('id')
    for  j in listofcourse:
        lcourse.append(j['id'])
    for j in lreg:
        lcourse.remove(j)
    listofcourses = []
    c =  courses.objects.filter(id__in=lcourse)
    for course in c:
        courseobj = listforstaff()
        courseobj.id = course.id
        courseobj.coursecode = course.coursecode
        courseobj.name = course.name
        courseobj.program = course.program
        listofcourses.append(vars(courseobj))
    d = faculty.objects.values_list('id','facultyname')
    listoffacs=[]
    for k in d:
        fobj = listforstaff()
        fobj.fid = k[0]
        fobj.fname = k[1]
        listoffacs.append(vars(fobj))
    
    return render(request, 'homeviews/partials/faculty_home_course_view_partial_unregistered.htm',{'courselist':json.dumps(listofcourses),  'listoffacs':json.dumps(listoffacs)})


def  student_course_partial_view(request):
    listofregcourses=reg_course.objects.all()
    studentuser = student.objects.get(rollnumber = request.user.username)
    l=[]
    for course in listofregcourses:
        c1 = courses.objects.get(id=course.courseid_id)
        if(c1.department.departmentcode == studentuser.department.departmentcode and len(reg_student.objects.filter(regcourseid_id=course.id,studentid_id=student.objects.get(rollnumber=request.user.username).id))==0):
            c = coursemodelforreg()
            c.id = course.id
            c.courseid = courses.objects.get(id=course.courseid_id).coursecode
            c.start = str(course.start)
            c.end = str(course.end)
            c.facultyname= faculty.objects.get(id=course.facultyid_id).facultyname
            c.coursename = courses.objects.get(id=course.courseid_id).name
            l.append(vars(c))
    return render(request, 'homeviews/partials/student_home_course_view_partial.htm',{'courselist':json.dumps(l), 'searchlabel':'Search courses'})

def student_regcourse_partial_view(request):
    l=[]
    for regc in reg_student.objects.filter(studentid_id=student.objects.get(rollnumber='B16008EC').id):
        course =courses.objects.get(id=reg_course.objects.get(id=regc.regcourseid_id).courseid_id)
        c = coursemodelforreg()
        c.id = course.id
        c.coursecode = course.coursecode
        c.coursename = course.name
        c.departmentname = department.objects.get(id=course.department_id).departmentname
        c.start  = str(reg_course.objects.get(id=regc.regcourseid_id).start)
        c.end = str(reg_course.objects.get(id=regc.regcourseid_id).end)
        c.facultyname = faculty.objects.get(id=reg_course.objects.get(id=regc.regcourseid_id).facultyid_id).facultyname
        l.append(vars(c))
    return render(request,'homeviews/partials/student_home_regcourse_view_partial.htm',{'courselist':json.dumps(l), 'searchlabel':'Search courses','username':request.user.username})
        

#Listing courses for stafff
def list_course_staff(request):
    coursesum = courses.objects.all()
    l=[]
    for c in coursesum:
        courselist   = listforstaff()
        courselist.coursecode = c.coursecode
        courselist.coursename = c.name
        courselist.program = programappings.objects.get(programcode=c.program).programtype
        courselist.department = department.objects.get(id=int(c.department_id)).departmentname
        l.append(vars(courselist))
    return render(request, 'homeviews/partials/staff_home_course_view_partial.htm',{'courselist':json.dumps(l)})


def list_student_staff(request):
    students = student.objects.all()
    l=[]
    for c in students:
        studentlist = listforstaff()
        studentlist.rollnumber  = c.rollnumber
        studentlist.studentname = c.name 
        studentlist.program = programappings.objects.get(programcode=c.program).programtype
        studentlist.department = department.objects.get(id=int(c.department_id)).departmentname
        studentlist.specialization = c.specialization
        l.append(vars(studentlist))
    return render(request, 'homeviews/partials/staff_home_student_view_partial.htm',{'studentlist':json.dumps(l)})

def list_faculty_staff(request):
    faculties = faculty.objects.all()
    l2=[]
    for c in faculties:
        facultylist = listforstaff()
        facultylist.facultyname = c.facultyname
        facultylist.isperm = c.isperm
        facultylist.department = department.objects.get(id=int(c.department_id)).departmentname
        facultylist.username = c.username
        facultylist.id = c.id
        l2.append(vars(facultylist))
    return render(request, 'homeviews/partials/staff_home_faculty_view_partial.htm',{'fac2':json.dumps(l2)})

def list_department_staff(request):
    departments = department.objects.all()
    l=[]
    for c in departments:
        departmentlist = listforstaff()
        departmentlist.departmentname = c.departmentname
        departmentlist.hod = c.hod
        departmentlist.code = c.departmentcode
        l.append(vars(departmentlist))
    return render(request, 'homeviews/partials/staff_home_department_view_partial.htm',{'departmentlist':json.dumps(l)})

def list_staff_staff(request):
    staffs = staff.objects.all()
    l = []
    for c in staffs:
        stafflist = listforstaff()
        stafflist.staffname = c.staffname
        stafflist.department= department.objects.get(id=int(c.department_id)).departmentname
        stafflist.username = c.username
        l.append(vars(stafflist))
    return render(request, 'homeviews/partials/staff_home_staff_view_partial.htm',{'stafflist':json.dumps(l)})


## Basic registration process.
def student_register_course(request):
    courseid = request.POST['registeredcourselist']
    courseid = courseid[1:-1]
    courseid = courseid.split(',')
    coursesregistered =0
    studentrollnumber = request.user.username
    for courseidforreg in courseid:
        studentid= student.objects.get(rollnumber=studentrollnumber).id
        reg_student.objects.create(regcourseid_id=courseidforreg,studentid_id=studentid)
        coursesregistered  = coursesregistered+1
    return render(request, 'homeviews/student_home.html',{'username':request.user.first_name, 'coursesregistered':coursesregistered})


def faculty_takeup_course(request):
    if(request.method=='GET'):
        objectlist =faculty.objects.values_list('facultyname', 'id')
        listoffacts=[]
        courselist = coursemodelforreg()
        courselist.id = request.GET['courseid']
        courselist.coursecode = request.GET['coursecode']
        courselist.name = request.GET['name']
        courselist.program = request.GET['program']
        for k in objectlist: 
            facts = facultymodelforcourse()
            facts.id = k[1]
            facts.name = k[0]
            listoffacts.append(facts)
        courselist.listoffaculties=listoffacts
        return render(request, 'homeviews/partials/faculty_home_course_view_partial_registering.htm',{'regcourse':courselist})
    else:
        #input_courseid = request.GET['courseid']
        #input_facultyid = request.GET['facultyid']
        #startdate= request.GET['startdate']
        #enddate=request.GET['enddate']
        #courses = courses.objects.get(id=courseid)
        #courses.reg_course_set.create(input_facultyid= start= ,end= )
        return render(request, 'homeviews/faculty_home.html',{})
    
def faculty_moveto_regcourses(request):
    courselists = request.POST['courselist']
    courselists = courselists[2:-2]
    courselists = courselists.split('","')
    startdate = request.POST['startdate']
    enddate = request.POST['enddate']
    inputfacultyid=request.POST['faculty_id']
    #courses1 = courses.objects.get(id=inputcourseid)
    #courses1.reg_course_set.create(facultyid_id=inputfacultyid, start=startdate, end = enddate)
    coursesmovedtoreg = 0
    for coursecodes in courselists:
        courses1 = courses.objects.get(coursecode=coursecodes) 
        courses1.reg_course_set.create(facultyid_id=inputfacultyid, start=startdate,end=enddate)
        coursesmovedtoreg = coursesmovedtoreg + 1
        #coursesmovedtoreg=coursesmovedtoreg+coursecodes
    return render(request, 'homeviews/faculty_home.html',{'coursemovedtoreg':coursesmovedtoreg})
    
def facutly_home(request):
    #courseid = request.GET['courseid']
    #coursecode = request.GET['coursecode']
    #coursename = request.GET['coursename']
    #program = request.GET['program']
    #facultyid = request.GET['facultyid']
    #courses = courses.objects.get(id=courseid)
    #courses.reg_course_set.create(facultyid_id=facultyid, start)
    return render(request, 'homeviews/faculty_home.html',{'username':request.user.first_name,'searchlabel':'Search courses' })

def student_home(request):
    return render(request, 'homeviews/student_home.html',{})
      
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/dmanager")
    
def loginpage(request):
    if(request.method=='POST'):
        form = LoginForm(request.POST)
        if(form.is_valid()):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if(user is not None):
                login(request,user)
                if('fac_' in user.username):
                    return render(request, 'homeviews/faculty_home.html',{'username':request.user.first_name})
                elif('staff_' in user.username):
                    return render(request, 'homeviews/staff_home.html',{'username':request.user.first_name})
                elif(student.objects.get(rollnumber=user.username)is not None):
                    return render(request, 'homeviews/student_home.html',{'username':request.user.username})
            else:
                pass
                return render(request, 'loginpage.html', {})
        else:
            return render(request, 'loginpage.html', {})
    else:
        form = LoginForm()
        return render(request, 'loginpage.html', {'form':  form.as_p()})

# ckass models
class facultymodelforcourse:
    pass

class coursemodelforreg:
    pass

class listforstaff:
    pass