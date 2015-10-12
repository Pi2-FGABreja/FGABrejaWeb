from django.test import TestCase
from django.test.utils import override_settings
from mock import patch
from api.sensor import SensorAPI
import requests


class TestSensor(TestCase):

    data = b'[{"type": [1, "themal"], "id": 4, "position": [1, "lower"], '\
           b'"location": [2, "second_pot"]}]'
    data_list = [{"type": [1, "themal"],
                  "id": 4, "position": [1, "lower"],
                  "location": [2, "second_pot"]}]

    def setUp(self):
        self.api = SensorAPI()

    @override_settings(API_URL='http://api.com')
    def test_get_url(self):
        url = self.api.get_url()
        self.assertEquals(url, 'http://api.com/sensors/')

    @override_settings(API_URL='http://api.com')
    def test_get_url_with_sensor_id(self):
        url = self.api.get_url(sensor_id=1)
        self.assertEquals(url, 'http://api.com/sensors/1/')

    @patch.object(requests, 'get')
    def test_get_data(self, mock):
        response = requests.Response()
        response._content = self.data
        mock.return_value = response

        sensor_data = self.api.get_data(self.api.get_url())
        self.assertEquals(sensor_data, self.data_list)

    @patch.object(SensorAPI, 'get_data')
    def test_all(self, mock):
        mock.return_value = self.data_list
        self.assertEquals(self.api.all(), self.data_list)
