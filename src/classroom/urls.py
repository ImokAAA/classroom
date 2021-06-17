from django.urls import include, path
from django.views.generic import TemplateView

from classroom.views import home

urlpatterns = [
    #path('home/', TemplateView.as_view(template_name = "classroom/templates/home.html"), name = 'home'),
]