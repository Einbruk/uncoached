from django.test import TestCase


class UsersViewTests(TestCase):
    def test_register(self):
        response = self.client.get('/users/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_login(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

