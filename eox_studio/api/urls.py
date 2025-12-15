""" urls.py """

from django.urls import include, re_path

app_name = 'eox_studio'  # pylint: disable=invalid-name

urlpatterns = [  # pylint: disable=invalid-name
    re_path(r'^v1/', include('eox_studio.api.v1.urls', namespace='eox-api')),
]
