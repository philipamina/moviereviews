#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:31:17 2022

@author: ochieng
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    ]
