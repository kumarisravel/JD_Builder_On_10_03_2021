from django.test import TestCase
from django.test import Client
# Create your tests here.

class SignUpTestCase(TestCase):
    def test_Sign_up(self):
        client=self.client.post('/signUp/',data={"email":"kumarisra@gmail.com","passwordConfirmed":"xyz","name":"kumar"})

        self.assertEqual(client.status_code,200)

