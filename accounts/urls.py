#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:26:09 2022

@author: ochieng
"""

from django.urls import path
from . import views

urlpatterns = [
    path('signupaccount/',views.signupaccount,name='signupaccount'),
    path('logout/',views.logoutaccount,name='logoutaccount'),
    path('login/',views.loginaccount,name='loginaccount')
    ]