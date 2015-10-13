from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from defaults.test import FGABrejaTestCase


class TestLoginView(FGABrejaTestCase):

    def test_put_method(self):
        response = self.client.put(reverse('login'))
        self.assertEquals(response.status_code, 405)

    def test_delete_methods(self):
        response = self.client.delete(reverse('login'))
        self.assertEquals(response.status_code, 405)

    def test_get(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')

    def test_get_logged(self):
        self.create_user()
        self.client.login(username='username', password='1234')
        response = self.client.get(reverse('login'))
        self.assertRedirects(response, '/')

    def test_post_valid_data(self):
        self.create_user()
        data = {'username': 'username', 'password': '1234',
                'next_url': '/auth/profile/'}
        self.client.post(reverse('login'), data=data)
        self.assertEqual(int(self.client.session['_auth_user_id']), 1)

    def test_post_invalid_password(self):
        self.create_user()
        data = {'username': 'username', 'password': 'invalid',
                'next_url': '/auth/profile/'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(200, response.status_code)

    def test_post_inactive_user(self):
        self.create_user(is_active=False)
        data = {'username': 'username', 'password': '1234',
                'next_url': '/auth/profile/'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(200, response.status_code)

    def test_next_url(self):
        data = {'username': 'username', 'password': '1234',
                'next_url': '/auth/profile/'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(200, response.status_code)


class TestLogoutView(FGABrejaTestCase):

    def test_get(self):
        self.create_user()
        self.client.login(username='username', password='1234')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/')


class TestUpdatePasswordView(FGABrejaTestCase):

    def setUp(self):
        self.data = {'password': 'password',
                     'confirm_password': 'password'}

    def test_post(self):
        self.create_user()
        self.client.login(username='username', password='1234')
        response = self.client.post(reverse('update_password'), data=self.data)
        self.assertRedirects(response, reverse('login'))

    def test_post_invalid_form(self):
        self.create_user()
        self.client.login(username='username', password='1234')
        self.data['confirm_password'] = '1234'
        response = self.client.post(reverse('update_password'), data=self.data)
        self.assertRedirects(response, reverse('user_profile'))


class TestForgotPasswordView(FGABrejaTestCase):

    def test_put_method(self):
        response = self.client.put(reverse('forgot_password'))
        self.assertEquals(response.status_code, 405)

    def test_delete_methods(self):
        response = self.client.delete(reverse('forgot_password'))
        self.assertEquals(response.status_code, 405)


class TestUserProfileView(FGABrejaTestCase):

    def setUp(self):
        self.data = {'first_name': 'first_name',
                     'email': 'email@test.com'}
        self.create_user()
        self.client.login(username='username', password='1234')

    def test_get(self):
        response = self.client.get(reverse('user_profile'))
        self.assertEquals(200, response.status_code)

    def test_post(self):
        response = self.client.post(reverse('user_profile'), data=self.data)
        self.assertRedirects(response, reverse('user_profile'))

    def test_post_invalid_data(self):
        self.data['email'] = 'invalid email'
        response = self.client.post(reverse('user_profile'), data=self.data)
        self.assertRedirects(response, reverse('user_profile'))


class TestRegisterUserView(FGABrejaTestCase):

    def setUp(self):
        self.data = {'username': 'username',
                     'first_name': 'first_name',
                     'email': 'email@test.com',
                     'password': 'password', }

    def test_put_method(self):
        response = self.client.put(reverse('register_user'))
        self.assertEquals(response.status_code, 405)

    def test_delete_methods(self):
        response = self.client.delete(reverse('register_user'))
        self.assertEquals(response.status_code, 405)

    def test_get(self):
        response = self.client.get(reverse('register_user'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_post_valid_data(self):
        before = len(User.objects.all())
        self.client.post(reverse('register_user'), data=self.data)
        after = len(User.objects.all())

        self.assertGreater(after, before)

    def test_post_invalid_username(self):
        self.data['username'] = 'invalid username !@#$'
        response = self.client.post(reverse('register_user'), data=self.data)
        self.assertRedirects(response, reverse('register_user'))

    def test_post_invalid_email(self):
        self.data['email'] = 'invalid email '
        response = self.client.post(reverse('register_user'), data=self.data)
        self.assertRedirects(response, reverse('register_user'))


class TestDeactivateUserView(FGABrejaTestCase):

    def setUp(self):
        self.create_user()
        self.client.login(username='username', password='1234')

    def test_post(self):
        response = self.client.post(reverse('deactivate_user'),
                                    data={'reason': 'reason'})
        self.assertRedirects(response, '/')
