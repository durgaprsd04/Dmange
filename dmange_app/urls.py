from django.urls import path

from . import views

app_name='dmange_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/', views.create_course, name='create_course'),
    path('finish_course', views.finish_course, name='finish_course'),
]

