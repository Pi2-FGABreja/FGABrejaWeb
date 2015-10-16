from django.http import HttpResponse
from django.core import serializers
from monitoring.models import ThermalSensor
import random


def get_sensor_data(request, sensor_id):
    sensors = ThermalSensor.objects.filter(identifier=sensor_id)
    data = serializers.serialize('json',
                                 [random.choice(sensors)],
                                 use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='application/json')
