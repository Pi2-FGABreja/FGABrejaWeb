from django.http import HttpResponse
from django.core import serializers
from monitoring.models import ThermalSensor
from django.shortcuts import render_to_response
from django.template import RequestContext
from defaults.views import FGABrejaView
import random


def get_sensor_data(request, sensor_id):
    sensors = ThermalSensor.objects.filter(identifier=sensor_id)
    data = serializers.serialize('json',
                                 [random.choice(sensors)],
                                 use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='application/json')


class HomeView(FGABrejaView):

    def get(self, request):
        sensor_data = ThermalSensor.objects.filter(
            identifier=1).order_by('date', 'time')
        return render_to_response('home.html', locals(),
                                  context_instance=RequestContext(request))
