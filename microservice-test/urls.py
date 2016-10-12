from django.conf.urls import url
from django.contrib import admin
from service.view import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/serviceA/$', DetailViewServiceA.as_view(), name = 'serviceA'),
    url(r'^api/serviceB/$', DetailViewServiceB.as_view(), name = 'serviceB'),
]
