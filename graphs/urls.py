from django.conf.urls import url, include
from .views import graphs

urlpatterns = [
    url(r'^graphs/$', graphs, name='graphs'),
]