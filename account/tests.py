from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.test import Client

from django.contrib.auth import login
from account.views import loginpediatrician,loginpsycholist
import unittest



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
class Testloginpsychologist(TestCase):
    def testcorrecrloginpsy(self):
        client = Client()
        response = client.post('loginpsycholist//', {'username':'testuser', 'password':'<PASSWORD>'})
        self.assertEqual(response.status_code, 200)

    def Testwrongusernameloginpsy(self):
        client = Client()
        response = client.post('loginpsycholist//', {'username': 'invalid', 'password': '<PASSWORD>'})
        self.assertEqual(response.status_code, 'username incorrect')

    def Testwrongpasswordloginpsy(self):
        client = Client()
        response = client.post('loginpsycholist//', {'username': 'testuser', 'password': 'wrong password'})
        self.assertEqual(response.status_code, 'password incorrect')

    def Testnothingusernamepasswordloginpsy(self):
        client = Client()
        response = client.post('loginpsycholist//', {'username': 'invalid', 'password': 'wrong password'})
        self.assertEqual(response.status_code, 'username and password incorrect')



