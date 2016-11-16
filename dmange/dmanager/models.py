from __future__ import unicode_literals
from django.db import models

# class department for departments    
class department(models.Model):
    departmentname = models.CharField(max_length=300)
    hod = models.CharField(max_length=300)
    departmentcode = models.CharField(max_length=100)

# a class which defines the student model
class student(models.Model):
    rollnumber = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=10)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    #username = models.CharField(max_length=100)
#can be used to define course model
class courses (models.Model):
    coursecode =models.CharField(max_length=30)
    name = models.CharField(max_length=300)
    program = models.CharField(max_length=300)
    department = models.ForeignKey(department, on_delete=models.CASCADE)

    
# a model which defines the faculties
class faculty(models.Model):
    facultyname = models.CharField(max_length=300)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    isperm=models.BooleanField()
    username = models.CharField(max_length=100)

# a model is for registered courses, courses which student can register and opt for an option.
class reg_course(models.Model):
    facultyid = models.ForeignKey(faculty, on_delete=models.CASCADE)
    courseid = models.ForeignKey(courses, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

# courses registered by students
class reg_student(models.Model):
    studentid = models.ForeignKey(student, on_delete=models.CASCADE)
    regcourseid = models.ForeignKey(reg_course, on_delete=models.CASCADE)

# for academic work as well as other stuff    
class staff(models.Model):
    staffname = models.CharField(max_length=300)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

# for things like rollnumber format, constant valued info which rarely changes, a key value pair set up.    
class defaultformats(models.Model):
    keyvalue = models.CharField(max_length=100)
    formatvalue=models.CharField(max_length=2000)

#these are the code mappings for programs(pg, ug, phd)
class programappings(models.Model):
    programtype = models.CharField(max_length=100)
    programcode = models.CharField(max_length=100)



