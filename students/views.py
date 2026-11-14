from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

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

def register_student(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-home')
    else:
        form = StudentForm()

    context = {
        'form': form, 
    }    
    return render(request,'students/register.html',context)

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student-home')
    return render(request, 'students/delete_student.html', {'student': student})