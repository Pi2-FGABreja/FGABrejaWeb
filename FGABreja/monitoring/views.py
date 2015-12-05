from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from defaults.views import FGABrejaView
from api.sensor import ThermalSensorAPI
import json


def get_temperature_average(request):
    api = ThermalSensorAPI()
    data = api.average()
    return HttpResponse(json.dumps(data), content_type='application/json')


class HomeView(FGABrejaView):

    def get(self, request):
        return render_to_response('home.html', locals(),
                                  context_instance=RequestContext(request))


class MonitoringView(FGABrejaView):

    def get(self, request):
        return render_to_response('monitoring.html', locals(),
                                  context_instance=RequestContext(request))


class NewProcessView(FGABrejaView):

    def get(self, request):
        return render_to_response('new_process.html', locals(),
                                  context_instance=RequestContext(request))
