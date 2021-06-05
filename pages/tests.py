from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class HomePageTest(TestCase):

    # homepage status code check
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # check by name
    def test_home_page_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # check template name
    def test_view_uses_template_name(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    # sign up page test


class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@gmail.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_current_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        newuser = get_user_model().objects.create_user(self.username,self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email)

