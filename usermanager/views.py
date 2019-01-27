# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'login.html')

#This is the home screen of the logged in user
def home(request):
    return render(request, 'home.html')