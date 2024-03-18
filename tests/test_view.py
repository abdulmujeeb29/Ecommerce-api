from rest_framework import status 
from rest_framework.response import Response 
from .test_setup import TestSetup


class UserTestCase(TestSetup):
    def test_register_endpoint(self):
        data = self.user_data
        response = self.client.post(self.register_url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)