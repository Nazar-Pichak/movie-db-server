from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Person

class PersonAPITest(APITestCase):
    def setUp(self):
        self.person = Person.objects.create(
            name="Testovací Herec",
            birth_date="1990-01-01",
            country="Česko",
            biography="Tady je krátká biografie.",
            role="actor"
        )
        
    def test_list_people(self):
        url = reverse("person-list")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Testovací Herec")
        self.assertEqual(response.data[0]["role"], "actor")