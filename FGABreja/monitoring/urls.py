from django.conf.urls import url
from monitoring.views import get_temperature_average, HomeView


urlpatterns = [
    url(r'^temperature/average/$', get_temperature_average,
        name='temperature_average'),
    url(r'^$', HomeView.as_view(), name='home'),
]
