#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:03:22 2022

@author: ochieng
"""

from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['watchAgain'].widget.attrs.update({
            'class': 'form-check-input'})
        
    class Meta:
        model = Review
        fields = ['text','watchAgain']
        labels = {'watchAgain': ('Watch Again')}
        widget = {'text': Textarea(attrs={'rows': 4}),}