from django.http import response
from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.views.generic.base import View
from ..views import students, teachers

def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request

def add_middleware_to_response(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request

class StudentViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_student_signup(self):
        request = self.factory.post('/accounts/signup/student/', {'email':'test@gmail.com', 'password1':'Pu$$yboy', 'password2':'Pu$$yboy'})
        
        request = add_middleware_to_request(request, SessionMiddleware)

        request.session.save()

        response = students.StudentSignUpView.as_view()(request)

        self.assertEqual(response.status_code, 302)
    '''
    def test_environment_set_in_context(self):
        request = self.factory.post('/accounts/signup/student/', {'email':'test@gmail.com', 'password1':'Pu$$yboy', 'password2':'Pu$$yboy'})
        view = students.StudentSignUpView().setup(request)

        context = view.get_context_data()
        self.assertIn('user_type', context)
        self.assertEqual(context['user_type'], 'student')
    '''