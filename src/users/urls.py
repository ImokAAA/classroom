from django.urls import include, path

from users.views import students,teachers

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #path('signup/', classroom.SignUpView.as_view(), name='signup'),
    path('signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]