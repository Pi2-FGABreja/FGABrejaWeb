from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from defaults.views import FGABrejaView
from api.sensor import ThermalSensorAPI
from api.controlling import ProcessAPI, RecipeAPI
import json


def get_temperature_average(request):
    api = ThermalSensorAPI()
    data = api.average()
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_actual_process(request):
    api = ProcessAPI()
    data = api.get_current_process()
    return HttpResponse(json.dumps(data), content_type='application/json')


class HomeView(FGABrejaView):

    def get(self, request):
        api = ProcessAPI()
        processes = api.all()
        return render_to_response('home.html', locals(),
                                  context_instance=RequestContext(request))


class MonitoringView(FGABrejaView):

    def get(self, request):
        return render_to_response('monitoring.html', locals(),
                                  context_instance=RequestContext(request))


class NewProcessView(FGABrejaView):

    def __init__(self):
        self.api = ProcessAPI()

    def get(self, request):
        api = RecipeAPI()
        recipes = api.all()
        return render_to_response('new_process.html', locals(),
                                  context_instance=RequestContext(request))

    def post(self, request):
        recipe_id = request.POST.get('recipe_id')
        self.api.create_process(recipe_id=recipe_id)
        return redirect('home')
