from django.shortcuts import render_to_response
from django.template import RequestContext
from defaults.views import FGABrejaView
from monitoring.models import ThermalSensor


class HomeView(FGABrejaView):

    def get(self, request):
        sensor_data = ThermalSensor.objects.filter(
            identifier=1).order_by('-date', '-time')
        return render_to_response('home.html', locals(),
                                  context_instance=RequestContext(request))
