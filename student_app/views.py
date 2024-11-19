
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Student
from .forms import StudentForm, StudentSearchForm

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_app/create_student.html', {'form': form})

@login_required
def view_student(request):
    student = None
    if request.method == 'POST':
        form = StudentSearchForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            student = get_object_or_404(Student, student_id=student_id)
    else:
        form = StudentSearchForm()
    return render(request, 'student_app/view_student.html', {
        'form': form,
        'student': student
    })

@login_required
@user_passes_test(is_admin)
def update_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_app/update_student.html', {
        'form': form,
        'student': student
    })

@login_required
@user_passes_test(is_admin)
def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    return render(request, 'student_app/delete_student.html', {'student': student})

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_app/student_list.html', {'students': students})
