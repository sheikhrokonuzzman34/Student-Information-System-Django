from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from student_app.models import Student


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']    




class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'class_name', 'teacher_name']

class StudentSearchForm(forms.Form):
    student_id = forms.CharField(max_length=20)
    
    


