from django.db import models

# Create your models here.
class Department(models.Model):
    department_code = models.CharField(primary_key=True)
    department_name = models.CharField(null=False)

class Course(models.Model):
    course_code = models.CharField(primary_key=True)
    department_code = models.ForeignKey(Department, on_delete = models.CASCADE)
    course_name = models.CharField(null=False)
    course_description = models.CharField()

class Facutly(models.Model):
    faculty_id = models.CharField(primary_key=True)
    faculty_name = models.CharField(null=False)
    department_code = models.ForeignKey(Department, on_delete = models.CASCADE)

class Student(models.Model):
    student_id = models.CharField(primary_key=True)
    student_name = models.CharField(null=False)
    department_code = models.ForeignKey(Department, on_delete=models.CASCADE)

class CourseForYear(models.Model):
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty_code = models.ForeignKey(Facutly, on_delete=models.CASCADE)
    year  = models.CharField(null=False)

class CourseRegistrationForYear(models.Model):
    course_for_year_id = models.ForeignKey(CourseForYear, on_delete = models.CASCADE)
    student_id = models.ForeignKey(CourseForYear, on_delete = models.CASCADE)
    