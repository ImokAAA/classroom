from django.test import TestCase
from ..models import User, Student

class StudentModelTest(TestCase):

    def setUp(self):
        email = 'Imangali02@gmail.com'
        password = 'Pu$$Y123123' 
        user = User.objects.create_user(email = email, password = password)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
    
    def test_user_email(self):
        user = User.objects.get(id=1)

        self.assertEqual('Imangali02@gmail.com', user.email)
    
    def test_student_user_relation(self):
        user = User.objects.get(id=1)
        student = Student.objects.get(user_id=1)
        
        self.assertTrue(user.is_student)
        self.assertEqual(user, student.user)