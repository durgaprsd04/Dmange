from django.db import models

# Create your models here.
class Department(models.Model):
    department_code = models.CharField(max_length=200)
    department_name = models.CharField(null=False,max_length=200)
    def __str__(self):
        return self.department_name

class Course(models.Model):
    course_code = models.CharField(max_length=200)
    department_code = models.ForeignKey(Department, on_delete = models.CASCADE)
    course_name = models.CharField(null=False,max_length=200)
    course_description = models.CharField(max_length=200)
    def __str__(self):
        return "%s %s %s"% (self.course_code, self.department_code, self.course_name) 

class Facutly(models.Model):
    faculty_id = models.CharField(max_length=200)
    faculty_name = models.CharField(null=False,max_length=200)
    department_code = models.ForeignKey(Department, on_delete = models.CASCADE)

class Student(models.Model):
    student_id = models.CharField(max_length=200)
    student_name = models.CharField(null=False, max_length=200)
    department_code = models.ForeignKey(Department, on_delete=models.CASCADE)

class CourseForYear(models.Model):
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty_id = models.CharField(null=False, max_length=200)
    year  = models.DateField(null=False)

class CourseRegistrationForYear(models.Model):
    course_for_year_id = models.ForeignKey(CourseForYear, on_delete = models.CASCADE)
    student_id =  models.CharField(max_length=200)
    