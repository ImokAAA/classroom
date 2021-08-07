from django.urls import path
from .views import AnswerAssignView, AnswerDetailView, AnswerListForTaskView, AnswerSubmitView
app_name = 'answer'
urlpatterns = [
    path('create/<int:pk>/<int:auditory_pk>', AnswerSubmitView.as_view(), name = 'create'),
    path('listfortask/<int:pk>/<int:auditory_pk>', AnswerListForTaskView.as_view(), name = 'list-task'),
    path('<int:pk>/<int:auditory_pk>', AnswerDetailView.as_view(), name = 'detail'),
    path('assign/<int:pk>/<int:auditory_pk>', AnswerAssignView.as_view(), name = 'assign'),
]