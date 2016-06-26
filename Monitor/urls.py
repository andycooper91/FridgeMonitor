# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:26:31 2016

@author: Andy
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update/(?P<user_id>[0-9]+)/(?P<kind_id>[0-9]+)$', views.update, name='update'),
]
