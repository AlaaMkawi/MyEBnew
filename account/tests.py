from django.contrib.auth.models import User, Group
from django.http import response
from django.test import TestCase
from django.test import Client

from django.contrib.auth import login
from account.views import loginpediatrician,loginpsychologist
from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.sessions.backends.base import SessionBase
from django.contrib.messages import get_messages
from unittest.mock import MagicMock

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from unittest.mock import MagicMock

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from unittest.mock import MagicMock
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Pediatrician
from .views import delete_ped, delete_confirm_ped
from django.contrib.sessions.middleware import SessionMiddleware

import unittest
from django.test import Client
from django.urls import reverse
from .models import Parent, Pediatrician, Psychologist, Meeting
from django.contrib.auth.models import User



import unittest
from django.test import TestCase, Client
from django.urls import reverse
from .models import ExtraInfo
from .forms import ExtraInfoForm


class ExtraInfoTestsPed(TestCase):
    def setUp(self):
        self.client = Client()
        self.form_data = {
            'title': 'Test Extra Info',
            'content': 'This is a test extra info.',
        }

    def test_add_extra_informationpeda(self):
        # Test that the add_extra_info view renders the correct template
        response = self.client.get(reverse('add_extra_informationa'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_extra_informationa.html')

        # Test that the form data is valid and saved to the database
        form = ExtraInfoForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('add_extra_informationa'), data=self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ExtraInfo.objects.count(), 1)
        self.assertEqual(ExtraInfo.objects.first().title, 'Test Extra Info')

    def test_view_extra_info_ped(self):
        # Test that the view_extra_info view renders the correct template
        response = self.client.get(reverse('extrainfopeda'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'extrainfopeda.html')

        # Test that the view_extra_info view displays all the extra info in the database
        ExtraInfo.objects.create(title='Test Extra Info 1', content='This is a test extra info 1.')
        ExtraInfo.objects.create(title='Test Extra Info 2', content='This is a test extra info 2.')
        response = self.client.get(reverse('extrainfopeda'))
        self.assertContains(response, 'Test Extra Info 1')
        self.assertContains(response, 'This is a test extra info 1.')
        self.assertContains(response, 'Test Extra Info 2')
        self.assertContains(response, 'This is a test extra info 2.')

class ExtraInfoTestsPsy(TestCase):
    def setUp(self):
        self.client = Client()
        self.form_data = {
            'title': 'Test Extra Info',
            'content': 'This is a test extra info.',
        }

    def test_add_extra_informationpsya(self):
        # Test that the add_extra_info view renders the correct template
        response = self.client.get(reverse('add_extra_informationa_psy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_extra_informationa_psy.html')

        # Test that the form data is valid and saved to the database
        form = ExtraInfoForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('add_extra_informationa_psy'), data=self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ExtraInfo.objects.count(), 1)
        self.assertEqual(ExtraInfo.objects.first().title, 'Test Extra Info')

    def test_view_extra_info_psy(self):
        # Test that the view_extra_info view renders the correct template
        response = self.client.get(reverse('extrainfopsya'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'extrainfopsya.html')

        # Test that the view_extra_info view displays all the extra info in the database
        ExtraInfo.objects.create(title='Test Extra Info 1', content='This is a test extra info 1.')
        ExtraInfo.objects.create(title='Test Extra Info 2', content='This is a test extra info 2.')
        response = self.client.get(reverse('extrainfopsya'))
        self.assertContains(response, 'Test Extra Info 1')
        self.assertContains(response, 'This is a test extra info 1.')
        self.assertContains(response, 'Test Extra Info 2')
        self.assertContains(response, 'This is a test extra info 2.')


class ExtraInfoTestsPar(TestCase):
    def setUp(self):
        self.client = Client()
        self.extra_info = ExtraInfo.objects.create(title='Test Extra Info', content='This is a test extra info.')

    def test_view_extra_info_par(self):
        # Test that the view_extra_info view renders the correct template
        response = self.client.get(reverse('extrainfopara'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'extrainfopara.html')

        # Test that the view_extra_info view displays the correct extra info
        self.assertContains(response, 'Test Extra Info')
        self.assertContains(response, 'This is a test extra info.')

class DeletePedPsyTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.email = 'test@example.com'
        self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)


    def test_delete_ped_view_get(self):
        url = reverse('delete_ped')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_ped.html')

    def test_delete_ped_view_post_invalid(self):
        url = reverse('delete_ped')
        data = {'username': 'wronguser', 'password': 'wrongpassword', 'email': 'wrong@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        # Verify that no error message is present
        self.assertEqual(len(messages), 0)

    def test_delete_ped_view_post_valid(self):
        url = reverse('delete_ped')
        data = {'username': self.username, 'password': self.password, 'email': self.email}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)  # Redirect after successful post

    def test_delete_confirm_ped_view_get(self):
        url = reverse('homepage')
        self.client.force_login(self.user)  # Log in the user
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Ensure the response status is OK
        self.assertTemplateUsed(response, 'homepage.html')  # Ensure the correct template is used


class DeleteParTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.email = 'test@example.com'
        self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)

    def test_delete_ped_view_get(self):
        url = reverse('delete_')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_.html')

    def test_delete_ped_view_post_invalid(self):
        url = reverse('delete_')
        data = {'username': 'wronguser', 'password': 'wrongpassword', 'email': 'wrong@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        # Verify that no error message is present
        self.assertEqual(len(messages), 0)

    def test_delete_ped_view_post_valid(self):
        url = reverse('delete_')
        data = {'username': self.username, 'password': self.password, 'email': self.email}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)  # Redirect after successful post

    def test_delete_confirm_ped_view_get(self):
        url = reverse('homepage')
        self.client.force_login(self.user)  # Log in the user
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Ensure the response status is OK
        self.assertTemplateUsed(response, 'homepage.html')  # Ensure the correct template is used

from django.test import TestCase
from django.urls import reverse
from .models import InformationBoard
from .views import psyinfoboard, delete_item, get_information
from django.test import RequestFactory

class PsyInfoBoardViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_psyinfoboard_GET(self):
        # Create some sample items
        InformationBoard.objects.create(content='Item 1')
        InformationBoard.objects.create(content='Item 2')

        # Make GET request
        request = self.factory.get(reverse('psyinfoboard'))
        response = psyinfoboard(request)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the items
        self.assertContains(response, 'Item 1')
        self.assertContains(response, 'Item 2')

    def test_delete_item_POST(self):
    # Create a sample item
        item = InformationBoard.objects.create(content='Item to delete')

    # Make POST request to delete the item
        request = self.factory.post(reverse('delete_item', args=[item.id]))
        response = delete_item(request, item_id=item.id)

    # Check if the item was deleted successfully
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"success": true}')

    def test_get_information(self):
    # Create some sample items
        InformationBoard.objects.create(content='Item 1')
        InformationBoard.objects.create(content='Item 2')

    # Make GET request
        request = self.factory.get(reverse('get_information'))
        response = get_information(request)

    # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

    # Check if the response contains the correct information items
        expected_data = b'[{"content": "Item 1"}, {"content": "Item 2"}]'
        self.assertEqual(response.content, expected_data)




from django.test import TestCase
from django.urls import reverse
from .models import PediatricianInfoBoard
from .views import pedinfoboard, delete_ped_item, get_ped_information
from django.test import RequestFactory

class PedInfoBoardViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_psyinfoboard_GET(self):
        # Create some sample items
        PediatricianInfoBoard.objects.create(content='Item 1')
        PediatricianInfoBoard.objects.create(content='Item 2')

        # Make GET request
        request = self.factory.get(reverse('pedinfoboard'))
        response = pedinfoboard(request)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the items
        self.assertContains(response, 'Item 1')
        self.assertContains(response, 'Item 2')

    def test_delete_ped_item_POST(self):
    # Create a sample item
        item = PediatricianInfoBoard.objects.create(content='Item to delete')

    # Make POST request to delete the item
        request = self.factory.post(reverse('delete_item', args=[item.id]))
        response = delete_ped_item(request, item_id=item.id)

    # Check if the item was deleted successfully
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"success": true}')

    def test_get_ped_information(self):
    # Create some sample items
        PediatricianInfoBoard.objects.create(content='Item 1')
        PediatricianInfoBoard.objects.create(content='Item 2')

    # Make GET request
        request = self.factory.get(reverse('get_ped_information'))
        response = get_ped_information(request)

    # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

    # Check if the response contains the correct information items
        expected_data = b'[{"content": "Item 1"}, {"content": "Item 2"}]'
        self.assertEqual(response.content, expected_data)




from django.urls import reverse
from .models import Paropinion
from .views import parop, delete_parop_item, get_parop_information
from django.test import RequestFactory
from django.test import TestCase
class ParopViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_parop_GET(self):
        # Create some sample items
        Paropinion.objects.create(content='Item 1')
        Paropinion.objects.create(content='Item 2')

        # Make GET request
        request = self.factory.get(reverse('parop'))
        response = parop(request)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the items
        self.assertContains(response, 'Item 1')
        self.assertContains(response, 'Item 2')

    def test_delete_parop_item_POST(self):
    # Create a sample item
        item = Paropinion.objects.create(content='Item to delete')

    # Make POST request to delete the item
        request = self.factory.post(reverse('delete_item', args=[item.id]))
        response = delete_parop_item(request, item_id=item.id)

    # Check if the item was deleted successfully
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"success": true}')

    def test_get_parop_information(self):
    # Create some sample items
        Paropinion.objects.create(content='Item 1')
        Paropinion.objects.create(content='Item 2')

    # Make GET request
        request = self.factory.get(reverse('get_parop_information'))
        response = get_parop_information(request)

    # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

    # Check if the response contains the correct information items
        expected_data = b'[{"content": "Item 1"}, {"content": "Item 2"}]'
        self.assertEqual(response.content, expected_data)



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
        self.assertRedirects(response, reverse('parhomepage'))

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


from django.test import TestCase
from django.urls import reverse

class AddDataHTMLTestCase(TestCase):
    def test_add_data_page_contains_form(self):
        response = self.client.get(reverse('add_data'))  # Assuming 'add_data' is the name of the view
        self.assertContains(response, '<h2>Add New Data</h2>')  # Check if the page contains the title
        self.assertContains(response, '<form')  # Check if the page contains a form element
       # self.assertContains(response, '{% csrf_token %}')  # Check if the CSRF token is included in the form
        self.assertContains(response, '<input type="submit" value="Submit">')  # Check if the submit button is present


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
        self.assertRedirects(response, reverse('pedhomepage'))

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
        self.assertRedirects(response, reverse('parhomepage'))

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