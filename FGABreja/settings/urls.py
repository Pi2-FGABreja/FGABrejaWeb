from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('authentication.urls')),
    url(r'^monitoring/', include('monitoring.urls')),
    url(r'^', include('home.urls')),
]
