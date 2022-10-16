#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 08:41:40 2022

@author: ochieng
"""
from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>', views.detail, name='detail'),
    path('<int:movie_id>/create', views.createreview,name='createreview'),
    path('review/<int:review_id>',views.updatereview,name='updatereview'),
    path('review/<int:review_id>/delete',views.deletereview,name='deletereview'),
    ]