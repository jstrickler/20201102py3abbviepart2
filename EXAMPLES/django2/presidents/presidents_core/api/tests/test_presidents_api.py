from rest_framework.test import APITestCase
from django.urls import reverse

class TestPresidentAPI(APITestCase):
    databases = ['potus']

    def setUp(self):
        print("HI MOM")
        self.gw = reverse('presidents-detail', args=[1])

    def test_null(self):

        result = self.client.get(self.gw)
        print(result)
