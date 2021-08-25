""" Support API urls.py """

from django.conf.urls import include, url

app_name = 'eox_studio'  # pylint: disable=invalid-name

urlpatterns = [  # pylint: disable=invalid-name
    url(r'^v1/', include('eox_studio.api.support.v1.urls', namespace='eox-support-api')),
]
