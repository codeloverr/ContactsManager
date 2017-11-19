from django.conf.urls import include,url
from .views import default


urlpatterns = [
    url(r'^$', default, name='default'),

]