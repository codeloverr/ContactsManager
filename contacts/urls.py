from django.conf.urls import url
from .views import default, search


urlpatterns = [
    url(r'^$', default, name='default'),
    url(r'^search', search, name='search'),

]