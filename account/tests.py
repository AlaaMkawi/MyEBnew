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

