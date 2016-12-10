from django.conf.urls import url
from . import views
app_name='dmanager'
urlpatterns = [
# ex: /polls/
    #Faculty Home and addition.
    url(r'^facultyhome$', views.facutly_home, name='faculty_home'),
	url(r'^faculty_takeup_course',views.faculty_takeup_course),
    url(r'^faculty_moveto_regcourses',views.faculty_moveto_regcourses),
    url(r'^edit_profile_faculty',views.edit_profile_faculty),
    url(r'^faculty_course_partial_view$', views.faculty_course_partial_view),
    
    
    url(r'^addcourse$', views.put_course, name='put_course'),
    url(r'^addstudent$', views.put_student, name='put_student'),
    url(r'^adddepartment',views.put_department, name='put_department'),
    url(r'^addfaculty',views.put_faculty, name='put_faculty'),
    url(r'^addstaff',views.put_staff, name='put_staff'),
    
    #Staff addition and view .Basic CURD permission for staff.
    ###adding data via partials for staff. no redirections
    url(r'^staff_student_input_form$', views.put_student, name='put_student'),
    url(r'^staff_course_input_form$', views.put_course, name='put_course'),
    url(r'^staff_department_input_form',views.put_department, name='put_department'),
    url(r'^staff_faculty_input_form',views.put_faculty, name='put_faculty'),
    url(r'^staff_staff_input_form',views.put_staff, name='put_staff'),
   
    #Staff course views. Applicable for faculties.
    url(r'^staff_course_partial_view', views.list_course_staff),
    url(r'^staff_student_partial_view', views.list_student_staff),
    url(r'^staff_faculty_partial_view', views.list_faculty_staff),
    url(r'^staff_department_partial_view', views.list_department_staff),
    url(r'^staff_staff_partial_view', views.list_staff_staff),
    ###Viewing registered courses various aggregation levels.abs
    url(r'^staff_regcourse_partial_view', views.list_regcourse_coursewise),
    url(r'^staff_regcoursestudent_partial_view',views.list_regcourse_studentwise1),
    url(r'^staff_regcoursefaculty_partial_view',views.list_regcourse_facultywise),
    url(r'^staff_regcoursefaculty_partial_courseview', views.list_regcourse_facultywise1),
    url(r'^staff_regcoursedepartment_partial_view',views.list_regcourse_departmentwise),
    url(r'^staff_regcoursedepartment_partial_courseview',views.list_regcourse_studentwise),
    #adding actions ot home button and DMange buttons
    url(r'^staff_stats_view_partial', views.list_stats_staff),
    url(r'^staff_home_view', views.staff_home_view),
    #Editing profiles
    url(r'^staff_edit_profile', views.staff_edit_profile),
    
    #deleting a faculty
    url(r'staff_faculty_delete', views.staff_faculty_delete),
    
    
    url(r'^logout',views.logout_user, name='logout_user'),
    #url(r'^listcourses$', views.list_courses, name='list_courses'),
    
    
    #student  views
    url(r'^student_course_partial_view', views.student_course_partial_view),
    url(r'^student_regcourse_partial_view',views.student_regcourse_partial_view),
    url(r'^student_regcourse_deregister_action',views.student_regcourse_deregister_action),
   
    
    
    url(r'^student_register_course$', views.student_register_course,name='student_register_course'),
    url(r'^studenthome$', views.student_home,name='student_home'),
	url(r'^$', views.loginpage, name='loginpage'),
    #url(r'^(?P<operator_id>[0-9]+)/$',views.detail,name='detail'),
	#url(r'^services',views.servicedetails,name='servicedetails'),
	#url(r'^selectservices', views.listofboardingpoints, name='listofboardingpoints'),
	#url(r'^selectservice',views.selectservice, name="selectservice"),
	#url(r'^serviceid=?[0-9]',views.bookservice, name='bookservice'),
]
