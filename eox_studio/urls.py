""" urls.py """

from django.urls import include, re_path

app_name = 'eox_studio'  # pylint: disable=invalid-name

urlpatterns = [  # pylint: disable=invalid-name
    re_path(r'^api/', include('eox_studio.api.urls', namespace='eox-api'))
]
