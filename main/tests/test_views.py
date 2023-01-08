from django.test import TestCase


class MainViewTests(TestCase):
    def test_landing(self):
        response = self.client.get('/landing/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/landing.html')
        self.assertContains(response, 'A platform')

    def test_main(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, '/year/2022/')

