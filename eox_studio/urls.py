""" urls.py """

from django.conf.urls import include, url

app_name = 'eox_studio'  # pylint: disable=invalid-name

urlpatterns = [  # pylint: disable=invalid-name
    url(r'^api/', include('eox_studio.api.urls', namespace='eox-api'))
]
