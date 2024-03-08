from django.test import TestCase

# Create your tests here.
from django.contrib.auth import login
from account.views import loginpediatrician,loginpsycholist
import unittest
from djang.contrib.auth.models import User, Group


class Testloginpediatrician(TestCase):
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



