# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:35:18 2018

@author: 乐大方
"""

from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
]