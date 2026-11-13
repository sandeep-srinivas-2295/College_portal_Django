from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student

def home(request):
    all_students = Student.objects.all()
    context = {
        'students': all_students,
    }
    return render(request, 'students/home.html', context)

def courses(request):
    subjects = [
        'Python & Django Web Development',
        'Database Management Systems (DBMS)',
        'Operating Systems',
        'Computer Networks',
        'Data Structures using C++',
    ]
    context = {
        'subject_list': subjects,
    }
    return render(request, 'students/courses.html', context)