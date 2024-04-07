from django.contrib.auth.models import User, Group
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import response, HttpResponseRedirect

from django.test import Client

from django.contrib.auth import login
from account.views import loginpediatrician,loginpsychologist
from django.test import TestCase
from django.urls import reverse


import unittest



"""class Testloginpediatrician(TestCase):
    def testcorrecrloginped(self):
        client = Client()
        response = client.post('loginpediatrician/', {'username':'testuser', 'password':'<PASSWORD>'})
        self.assertEqual(response.status_code, 200)

    def Testwrongusernameloginped(self):
        client = Client()
        response = client.post('loginpediatrician/', {'username': 'invalid', 'password': '<PASSWORD>'})
        self.assertEqual(response.status_code, 'username incorrect')

    def Testwrongpasswordloginped(self):
        client = Client()
        response = client.post('loginpediatrician/', {'username': 'testuser', 'password': 'wrong password'})
        self.assertEqual(response.status_code, 'password incorrect')

    def Testnothingusernamepasswordloginped(self):
        client = Client()
        response = client.post('loginpediatrician/', {'username': 'invalid', 'password': 'wrong password'})
        self.assertEqual(response.status_code, 'username and password incorrect')
class Testloginpsychologist(TestCase):
    def testcorrecrloginpsy(self):
        client = Client()
        response = client.post('loginpsychologist//', {'username':'testuser', 'password':'<PASSWORD>'})
        self.assertEqual(response.status_code, 200)

    def Testwrongusernameloginpsy(self):
        client = Client()
        response = client.post('loginpsychologist//', {'username': 'invalid', 'password': '<PASSWORD>'})
        self.assertEqual(response.status_code, 'username incorrect')

    def Testwrongpasswordloginpsy(self):
        client = Client()
        response = client.post('loginpsychologist//', {'username': 'testuser', 'password': 'wrong password'})
        self.assertEqual(response.status_code, 'password incorrect')

    def Testnothingusernamepasswordloginpsy(self):
        client = Client()
        response = client.post('loginpsychologist//', {'username': 'invalid', 'password': 'wrong password'})
        self.assertEqual(response.status_code, 'username and password incorrect')"""




from django.contrib.auth.models import User, Group
from django.test import TestCase, Client
from django.urls import reverse

class TestLoginPsychologist(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('loginpsychologist')
        self.group = Group.objects.create(name='Psychologist')
        self.user = User.objects.create_user(username='testpsychologist', password='testpassword')
        self.user.groups.add(self.group)

    def test_correct_login(self):
        response = self.client.post(self.url, {'username': 'testpsychologist', 'password': 'testpassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('homepageforpys'))

    def test_incorrect_username(self):
        response = self.client.post(self.url, {'username': 'invalidusername', 'password': 'testpassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password incorrect')

    def test_incorrect_password(self):
        response = self.client.post(self.url, {'username': 'testpsychologist', 'password': 'invalidpassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password incorrect')

    def test_missing_username_or_password(self):
        response = self.client.post(self.url, {'username': '', 'password': ''}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password incorrect')


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.messages import get_messages
from django.contrib import messages

class TestLoginPediatrician(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('loginpediatrician')
        self.group = Group.objects.create(name='pediatrician')
        self.user = User.objects.create_user(username='testpediatrician', password='testpassword')
        self.user.groups.add(self.group)

    def test_correct_login(self):
        response = self.client.post(self.url, {'username': 'testpediatrician', 'password': 'testpassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('homepagefordoctors'))

    def test_incorrect_username(self):
        response = self.client.post(self.url, {'username': 'invalidusername', 'password': 'testpassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password incorrect')

    def test_incorrect_password(self):
        response = self.client.post(self.url, {'username': 'testpediatrician', 'password': 'invalidpassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password incorrect')

    def test_missing_username_or_password(self):
        response = self.client.post(self.url, {'username': '', 'password': ''}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password incorrect')

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.messages import get_messages
from django.contrib import messages

class TestLoginParent(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('loginParent')
        self.group = Group.objects.create(name='Parent')
        self.user = User.objects.create_user(username='testparent', password='testpassword')
        self.user.groups.add(self.group)

    def test_correct_login(self):
        response = self.client.post(self.url, {'username': 'testparent', 'password': 'testpassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('homepageforparents'))

    def test_incorrect_username(self):
        response = self.client.post(self.url, {'username': 'invalidusername', 'password': 'testpassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password incorrect')

    def test_incorrect_password(self):
        response = self.client.post(self.url, {'username': 'testparent', 'password': 'invalidpassword'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password incorrect')

    def test_missing_username_or_password(self):
        response = self.client.post(self.url, {'username': '', 'password': ''}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password incorrect')
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestSignUp(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('signup')

    def test_get_signup_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_new_user(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_signup_existing_user(self):
        # Create a user with the same username
        User.objects.create_user(username='existinguser', email='existing@example.com', password='ExistingPassword123')
        data = {
            'username': 'existinguser',
            'email': 'test@example.com',  # Same email as existing user
            'password1': 'TestPassword123',
            'password2': 'TestPassword123'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        self.assertFalse(User.objects.filter(email='test@example.com').exists())

    def test_signup_password_mismatch(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'TestPassword123',
            'password2': 'DifferentPassword'  # Different password
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        self.assertFalse(User.objects.filter(username='testuser').exists())


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class TestSignUp(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('signupys')  # תיקון כאן לשם הנכון של ה-URL

    # כאן כדאי להוסיף פונקציה שתיצור משתמש קיים כדי לבדוק את הרישום של משתמש קיים.
    # לדוגמה:
    def create_existing_user(self):
        User.objects.create_user(username='existinguser', password='TestPassword123')

    def test_get_signup_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signupys.html')

    def test_signup_new_user(self):
        data = {
            'username': 'testuser',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_signup_existing_user(self):
        self.create_existing_user()  # קריאה לפונקציה שיצרנו
        data = {
            'username': 'existinguser',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        self.assertTrue(User.objects.filter(username='existinguser').exists())

    def test_signup_password_mismatch(self):
        data = {
            'username': 'testuser',
            'password1': 'TestPassword123',
            'password2': 'DifferentPassword'  # Different password
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        self.assertFalse(User.objects.filter(username='testuser').exists())


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class TestSignUp(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('signuped')

    def test_get_signup_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signuped.html')

    def test_signup_new_user(self):
        data = {
            'username': 'testuser',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_signup_existing_user(self):
        # Create a user with the same username
        User.objects.create_user(username='existinguser', password='ExistingPassword123')
        data = {
            'username': 'existinguser',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        self.assertTrue(User.objects.filter(username='existinguser').exists())

    def test_signup_password_mismatch(self):
        data = {
            'username': 'testuser',
            'password1': 'TestPassword123',
            'password2': 'DifferentPassword'  # Different password
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        self.assertFalse(User.objects.filter(username='testuser').exists())





from django.test import TestCase
from django.urls import reverse

class AddDataHTMLTestCase(TestCase):
    def test_add_data_page_contains_form(self):
        response = self.client.get(reverse('add_data'))  # Assuming 'add_data' is the name of the view
        self.assertContains(response, '<h2>Add New Data</h2>')  # Check if the page contains the title
        self.assertContains(response, '<form')  # Check if the page contains a form element
       # self.assertContains(response, '{% csrf_token %}')  # Check if the CSRF token is included in the form
        self.assertContains(response, '<input type="submit" value="Submit">')  # Check if the submit button is present


from django.test import TestCase
from django.urls import reverse
from .models import BabyHealth


class ViewDataTestCase(TestCase):
    def test_view_data_page(self):
        # יצירת מידע לבדיקה
        BabyHealth.objects.create(name="Test Baby", description="Test description")

        # בצע בקשת GET לדף view_data
        response = self.client.get(reverse('view_data'))

        # אמור לקבל קוד תגובה 200 (הצלחה)
        self.assertEqual(response.status_code, 200)

        # אמור לקבל תוכן הכולל את שם ותיאור המידע שנוצר
        self.assertContains(response, "Test Baby")
        self.assertContains(response, "Test description")


from django.test import TestCase
from django.urls import reverse
from .models import Comment
from .forms import CommentForm


class SubmitCommentTestCase(TestCase):
    def test_submit_comment_GET(self):
        # בדיקת תגובת GET לדף submit_comment
        response = self.client.get(reverse('submit_comment'))
        self.assertEqual(response.status_code, 200)  # אמור לקבל קוד תגובה 200

        # בדיקה שהטופס נכנס לתוך התגית form
        self.assertContains(response, '<form')
        self.assertContains(response, '</form>')
        self.assertIsInstance(response.context['comment_form'], CommentForm)  # בדיקה שהטופס במשתנה ההקשר

    def test_submit_comment_POST_valid_form(self):
        # יצירת מידע לבדיקה
        post_data = {'comment_text': 'Test comment'}

        # בדיקת תגובת POST עם טופס תקין
        response = self.client.post(reverse('submit_comment'), data=post_data)
        self.assertRedirects(response, reverse('thank_you'))  # אמור להוביל לדף thank_you

        # בדיקה שהתגובה יצרה את התגובה בבסיס הנתונים
        self.assertTrue(Comment.objects.filter(comment_text='Test comment').exists())

    def test_submit_comment_POST_invalid_form(self):
        # בדיקת תגובת POST עם טופס לא תקין
        response = self.client.post(reverse('submit_comment'), data={})
        self.assertEqual(response.status_code, 200)  # אמור לקבל קוד תגובה 200

        # בדיקה שהטופס לא תקין נשלח חזרה לדף
        self.assertContains(response, '<form')
        self.assertContains(response, '</form>')
        self.assertIsInstance(response.context['comment_form'], CommentForm)  # בדיקה שהטופס במשתנה ההקשר


from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class FeedbackSubmitTestCase(TestCase):
    def test_feedback_submit_view(self):
        # יצירת לקוח דמי
        client = Client()

        # שליחת בקשת POST ל-View
        response = client.post(reverse('feedback_submit'),
                               {'your_name': 'Test User', 'message': 'This is a test message.'})

        # אימות כי התשובה חייבת להיות קוד תגובה 302 (התחזרה לדף תודה)
        self.assertEqual(response.status_code, 200)
