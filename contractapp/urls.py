"""Url redirections shoud be done from here"""
from django.conf.urls import url
# from django.contrib import admin
from contractapp.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^login$', login, name='login'),
    url(r'^home$', home, name='home'),
    # url(r'^gettime$', gettime, name='gettime'),
    url(r'^accounts/login/$', index),
    url(r'^createpsc/$', createpsc),
    # url(r'^import_data/$',import_data,name='import_data'),
    url(r'^pageredirect/(?P<name>\w+)/$', pageredirect, name='pageredirect')
]
