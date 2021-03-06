from classroom.views import AuditoryAddStudentView, AuditoryCreateView, AuditoryDetailView, AuditoryListView, TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView, AuditoryDeleteView
from django.urls import path

app_name = 'classroom'
urlpatterns = [
    path('list/', AuditoryListView.as_view(), name = 'list'),
    path('<int:pk>', AuditoryDetailView.as_view(), name = 'detail'),
    path('create', AuditoryCreateView.as_view(), name = 'create'),
    path('delete/<int:pk>', AuditoryDeleteView.as_view(), name = 'delete'),
    path('<int:pk>/add_student', AuditoryAddStudentView.as_view(), name = 'add_student'),
    path('task/list/<int:pk>', TaskListView.as_view(), name = 'task-list'),
    path('task/<int:auditory_pk>/<int:pk>', TaskDetailView.as_view(), name = 'task-detail'),
    path('task/create/<int:pk>', TaskCreateView.as_view(), name = 'task-create'),
    path('task/delete/<int:auditory_pk>/<int:pk>', TaskDeleteView.as_view(), name = 'task-delete'),
]