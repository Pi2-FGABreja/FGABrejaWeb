from django.test import TestCase
from defaults.forms import FGABrejaForm
from mock import Mock


class TestDefaultsForm(TestCase):

    def setUp(self):
        self.data = {'data': 'data', }
        request = Mock(POST=self.data)
        self.form = FGABrejaForm(request)

    def test_is_valid(self):
        with self.assertRaises(NotImplementedError):
            self.form.is_valid()

    def test_save(self):
        with self.assertRaises(NotImplementedError):
            self.form.save()
