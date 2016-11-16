from django.contrib import admin

# Register your models here.

from .models import student,courses, department, faculty, reg_course, reg_student, staff
# Register your models here.

admin.site.register(student)
admin.site.register(courses)
admin.site.register(department)
admin.site.register(faculty)
admin.site.register(reg_course)
admin.site.register(reg_student)
admin.site.register(staff)

