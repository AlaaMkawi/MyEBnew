from django.contrib.auth.models import User, Group
from django.http import response
from django.test import TestCase
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

from .models import Feedback
from .forms import FeedbackForm
from .views import feedbackl
class FeedbackViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_feedback_view_template(self):
        request = self.factory.get(reverse('feedbackl'))
        response = feedbackl(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedbackl.html')

    def test_feedback_view_GET(self):
        request = self.factory.get(reverse('feedbackl'))
        response = feedbackl(request)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], FeedbackForm)

    def test_feedback_view_POST_valid_form(self):
        request = self.factory.post(reverse('feedbackl'), data={'your_form_data_here'})
        response = feedbackl(request)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertRedirects(response, reverse('feedbackl'))  # Redirecting back to the feedback page

        # Check if the form data is saved
        self.assertEqual(Feedback.objects.count(), 1)
        saved_feedback = Feedback.objects.first()
        self.assertEqual(saved_feedback.your_field_name_here, 'expected_value')
from .models import InformationBoard
from .views import psyinfoboard

class PsyInfoBoardViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_psyinfoboard_POST(self):
        request = self.factory.post(reverse('psyinfoboard'), data={'content': 'Test content'})
        response = psyinfoboard(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('item_id', response.json())  # Check if the response contains 'item_id'

        # Check if an item is created in the database
        self.assertEqual(InformationBoard.objects.count(), 1)
        item = InformationBoard.objects.first()
        self.assertEqual(item.content, 'Test content')

    def test_psyinfoboard_GET(self):
        # Create sample items in the database
        InformationBoard.objects.create(content='Item 1')
        InformationBoard.objects.create(content='Item 2')

        request = self.factory.get(reverse('psyinfoboard'))
        response = psyinfoboard(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'psyinfoboard.html')

        # Check if existing items are passed to the template
        self.assertEqual(len(response.context['items']), 2)
        self.assertEqual(response.context['items'][0].content, 'Item 1')
        self.assertEqual(response.context['items'][1].content, 'Item 2')

from .views import delete_item, get_information

class DeleteItemViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_delete_item_POST(self):
        # Create a sample item in the database
        item = InformationBoard.objects.create(content='Test content')

        request = self.factory.post(reverse('delete_item', args=[item.id]))
        response = delete_item(request, item_id=item.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': True})

        # Check if the item is deleted from the database
        self.assertFalse(InformationBoard.objects.filter(id=item.id).exists())

class GetInformationViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_information(self):
        # Create sample items in the database
        InformationBoard.objects.create(content='Item 1')
        InformationBoard.objects.create(content='Item 2')

        request = self.factory.get(reverse('get_information'))
        response = get_information(request)
        self.assertEqual(response.status_code, 200)

        # Check if the returned JSON contains the correct information items
        expected_data = [{'content': 'Item 1'}, {'content': 'Item 2'}]
        self.assertListEqual(response.json(), expected_data)
from .models import PediatricianInfoBoard
from .views import pedinfoboard, delete_ped_item, get_ped_information

class PedInfoBoardViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_pedinfoboard_POST(self):
        request = self.factory.post(reverse('pedinfoboard'), data={'content': 'Test content'})
        response = pedinfoboard(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('item_id', response.json())  # Check if the response contains 'item_id'

        # Check if an item is created in the database
        self.assertEqual(PediatricianInfoBoard.objects.count(), 1)
        item = PediatricianInfoBoard.objects.first()
        self.assertEqual(item.content, 'Test content')

    def test_pedinfoboard_GET(self):
        # Create sample items in the database
        PediatricianInfoBoard.objects.create(content='Item 1')
        PediatricianInfoBoard.objects.create(content='Item 2')

        request = self.factory.get(reverse('pedinfoboard'))
        response = pedinfoboard(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pedinfoboard.html')

        # Check if existing items are passed to the template
        self.assertEqual(len(response.context['items']), 2)
        self.assertEqual(response.context['items'][0].content, 'Item 1')
        self.assertEqual(response.context['items'][1].content, 'Item 2')

class DeletePedItemViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_delete_ped_item_POST(self):
        # Create a sample item in the database
        item = PediatricianInfoBoard.objects.create(content='Test content')

        request = self.factory.post(reverse('delete_ped_item', args=[item.id]))
        response = delete_ped_item(request, item_id=item.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': True})

        # Check if the item is deleted from the database
        self.assertFalse(PediatricianInfoBoard.objects.filter(id=item.id).exists())

class GetPedInformationViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_ped_information(self):
        # Create sample items in the database
        PediatricianInfoBoard.objects.create(content='Item 1')
        PediatricianInfoBoard.objects.create(content='Item 2')

        request = self.factory.get(reverse('get_ped_information'))
        response = get_ped_information(request)
        self.assertEqual(response.status_code, 200)

        # Check if the returned JSON contains the correct information items
        expected_data = [{'content': 'Item 1'}, {'content': 'Item 2'}]
        self.assertListEqual(response.json(), expected_data)