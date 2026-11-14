from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='student-home'),
    path('courses/', views.courses, name='student-courses'),
    path('register/',views.register_student, name='student-register'),
    path('edit/<int:pk>/',views.edit_student, name='student-edit'),
    path('delete/<int:pk>/',views.delete_student, name='student-delete'),
]