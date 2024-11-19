from django.urls import path
from student_app.views import *

urlpatterns = [
    path('', student_list, name='student_list'),
    path('create/', create_student, name='create_student'),
    path('view/', view_student, name='view_student'),
    path('update/<str:student_id>/', update_student, name='update_student'),
    path('delete/<str:student_id>/', delete_student, name='delete_student'),
    
    # authentication
    
    path('login/', login_view, name='login'),
    path('register/',register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]