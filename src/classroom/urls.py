from classroom.views import AuditoryAddStudentView, AuditoryCreateView, AuditoryDetailView, AuditoryListView, TaskDetailView, TaskListView, AuditoryDeleteView
from django.urls import path

app_name = 'classroom'
urlpatterns = [
    #path('home/', TemplateView.as_view(template_name = "classroom/templates/home.html"), name = 'home'),
    path('list/', AuditoryListView.as_view(), name = 'list'),
    path('<int:pk>', AuditoryDetailView.as_view(), name = 'detail'),
    path('create', AuditoryCreateView.as_view(), name = 'create'),
    path('delete/<int:pk>', AuditoryDeleteView.as_view(), name = 'delete'),
    path('<int:pk>/add_student', AuditoryAddStudentView.as_view(), name = 'add_student'),
    path('task/list/', TaskListView.as_view(), name = 'task-list'),
    path('task/<int:pk>', TaskDetailView.as_view(), name = 'task-detail'),
]