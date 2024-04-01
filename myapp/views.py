from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students_list = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    return render(request, 'myapp/students.html', {'students_list': students_list, 'form': form})

def courses(request):
    courses_list = Course.objects.all()
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    return render(request, 'myapp/courses.html', {'courses_list': courses_list, 'form': form})

def student_details(request, student_id):
    student = Student.objects.get(id=student_id)
    not_registered_courses = Course.objects.exclude(students=student)
    return render(request, 'myapp/details.html', {'student': student, 'not_registered_courses': not_registered_courses})

def add_course(request):
    return render(request, 'myapp/add_course.html') 