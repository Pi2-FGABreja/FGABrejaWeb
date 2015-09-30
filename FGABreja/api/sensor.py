# from monitoring.models import TermalSensor
from django.conf import settings
import requests


class SensorAPI(object):

    def get_url(self, sensor_id=None):
        url = settings.API_URL
        if sensor_id:
            url += "/sensors/{}".format(sensor_id)
        else:
            url += "/sensors/"
        return url

    def get_data(self, url):
        response = requests.get(url)
        return response.json()

    def all(self):
        return self.get_data(self.get_url())
