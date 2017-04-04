from django.conf.urls import url, include
from django.contrib import admin
# from contractapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contractapp/',include("contractapp.urls")),
    # url(r'^$', index),
    # url(r'^login$', login, name='login'),
    # url(r'^home$', home, name='home'),
    # url(r'^gettime$', gettime, name='gettime'),
    # url(r'^accounts/login/$', index)   
]
