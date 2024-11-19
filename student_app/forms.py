from django import forms
from student_app.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'class_name', 'teacher_name']

class StudentSearchForm(forms.Form):
    student_id = forms.CharField(max_length=20)

