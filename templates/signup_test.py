from django.test import TestCase
from django.urls import reverse
from hypothesis import given, strategies as st
from django.contrib.auth.models import User

class SignUpFormTests(TestCase):
    @given(st.text(min_size=1), st.text(min_size=8)) 
    def test_signup_form_submission(self, username, password):
        form_data = {
            'username': username,
            'password': password,
        }
        response = self.client.post(reverse('signup'), data=form_data)
        self.assertEqual(response.status_code, 200)
