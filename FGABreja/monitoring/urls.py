from django.conf.urls import url
from monitoring.views import get_sensor_data


urlpatterns = [
    url(r'^sensor/(?P<sensor_id>[0-9]+)$', get_sensor_data,
        name='get_sensor_data'),
]
