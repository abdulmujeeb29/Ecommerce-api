from rest_framework.test import APITestCase 
from faker import Faker 
from django.urls import reverse 


class TestSetup(APITestCase):
    def setUp(self):
        self.fake =Faker()
        self.register_url = reverse('register-user')

        self.user_data = {
            'username' : self.fake.user_name(),
            'email' : self.fake.email(),
            'first_name' : self.fake.first_name(),
            'last_name' : self.fake.last_name(),
            'password' : self.fake.password()

        }
        