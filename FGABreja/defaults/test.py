from django.test import TestCase, Client
from django.contrib.auth.models import User


class FGABrejaTestCase(TestCase):

    client = Client()

    def create_user(self, is_active=True):
        user = User()
        user.id = 1
        user.username = 'username'
        user.email = 'email@test.com'
        user.first_name = 'first'
        user.set_password('1234')
        user.is_active = is_active
        user.save()
