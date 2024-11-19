
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Student
from .forms import StudentForm, StudentSearchForm


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

from django.contrib.auth import logout

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('student_list')
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('student_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect('login')

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

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_app/student_list.html', {'students': students})
