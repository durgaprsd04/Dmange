from django import forms
from .models import department, programappings

class StudentForm(forms.Form):
    #rollnumber = forms.CharField(label="Roll number", max_length=300)
    name = forms.CharField(label="Name of student", max_length=100)
    dpt_choices= programappings.objects.values_list('programcode', 'programtype')
    program =forms.ChoiceField(dpt_choices, required=False, widget= forms.Select())
    specialization =forms.CharField(label="Specialization", max_length=100)
    dpt_choices= department.objects.values_list('departmentcode', 'departmentname')
    department = forms.ChoiceField(dpt_choices, required=False, widget= forms.Select())

class DepartmentForm(forms.Form):
    departmentname = forms.CharField(label="Department Name", max_length=1000)
    hodname = forms.CharField(label="HOD", max_length=300)
    departmentcode = forms.CharField(label="Department Code", max_length=200)
    
class CourseForm(forms.Form):
    name = forms.CharField(label="Course name", max_length=300)
    dpt_choices= programappings.objects.values_list('programcode', 'programtype')
    program =forms.ChoiceField(dpt_choices, required=False, widget= forms.Select())
    dpt_choices= department.objects.values_list('departmentcode', 'departmentname')
    department = forms.ChoiceField(dpt_choices, required=False, widget= forms.Select())

class FacultyForm(forms.Form):
    facultyname = forms.CharField(label="Faculty name", max_length=300)
    dpt_choices= department.objects.values_list('departmentcode', 'departmentname')
    department = forms.ChoiceField(dpt_choices, required=False, widget= forms.Select())
    isperm = forms.BooleanField(label='Is Permanent')
    username = forms.CharField(label="Username",max_length=300)

    
class StaffForm(forms.Form):
    staffname = forms.CharField(label="Staff name",max_length=300)
    dpt_choices= department.objects.values_list('departmentcode', 'departmentname')
    department = forms.ChoiceField(dpt_choices, required=False, widget= forms.Select())
    staffusername = forms.CharField(label="Staff name",max_length=300)
    
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=300)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    