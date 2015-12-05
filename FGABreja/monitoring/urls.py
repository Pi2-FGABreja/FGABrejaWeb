from django.conf.urls import url
from monitoring.views import (get_temperature_average, HomeView,
                              NewProcessView, MonitoringView)


urlpatterns = [
    url(r'^temperature/average/$', get_temperature_average,
        name='temperature_average'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^monitoring/$', MonitoringView.as_view(), name='monitoring'),
    url(r'^process/new$', NewProcessView.as_view(), name='new_process'),
]
