from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='student-home'),
    path('courses/', views.courses, name='student-courses'),
]