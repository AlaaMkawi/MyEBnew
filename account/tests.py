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


class TestViews(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.client = Client()

    def test_parent_profView(self):
        # Create a parent object for testing
        parent = Parent.objects.create(name="Test Parent")

        # Get the URL for parent_profView and pass the parent's id
        url = reverse('parent_profView', args=[parent.id])

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

    def test_pediatrician_profView(self):
        # Create a pediatrician object for testing
        pediatrician = Pediatrician.objects.create(name="Test Pediatrician")

        # Get the URL for pediatrician_profView and pass the pediatrician's id
        url = reverse('pediatrician_profView', args=[pediatrician.id])

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

    def test_psychologist_profView(self):
        # Create a psychologist object for testing
        psychologist = Psychologist.objects.create(name="Test Psychologist")

        # Get the URL for psychologist_profiView
        url = reverse('psychologist_profView')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)



    def test_Parent_profile(self):
        # Login a user
        user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(user)

        # Get the URL for Parent_profile
        url = reverse('Parent_profile')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

    def test_Parent_editProfile_GET(self):
        # Login a user
        user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(user)

        # Get the URL for Parent_editProfile
        url = reverse('Parent_editProfile')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

    # Add more tests for POST request of Parent_editProfile if needed

    def test_Ped_profile(self):
        # Login a user
        user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(user)

        # Get the URL for Ped_profile
        url = reverse('Ped_profile')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

    def test_Ped_editProfile_GET(self):
        # Login a user
        user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(user)

        # Get the URL for Ped_editProfile
        url = reverse('Ped_editProfile')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

    # Add more tests for POST request of Ped_editProfile if needed

    def test_Psy_profile(self):
        # Login a user
        user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(user)

        # Get the URL for Psy_profile
        url = reverse('Psy_profile')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

    def test_Psy_editProfile_GET(self):
        # Login a user
        user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_login(user)

        # Get the URL for Psy_editProfile
        url = reverse('Psy_editProfile')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

    # Add more tests for POST request of Psy_editProfile if needed

    def test_meeting_board(self):
        # Get the URL for meeting_board
        url = reverse('meeting_board')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check if the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
