# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def loginpage(request):
    if(request.user.is_authenticated):
        return redirect(reverse('home'))
    return render(request, 'login.html')

#This is the home screen of the logged in user
@login_required
def home(request):
    return render(request, 'home.html')

#Verify the login process
def verify_login(request):
    if(request.user.is_authenticated):
        return redirect('home')
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if(user is not None):
            login(request, user)
            return redirect(reverse("home"))
    return redirect(reverse('login'))

#create account
def create_account(request):
	if(request.user.is_authenticated):
		return redirect(reverse('home'))
	if(request.method == "POST"):
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		username = request.POST["create_username"]
		password = request.POST["create_password"]
		confirm_password = request.POST["confirm_password"]
		if(password != confirm_password):
			return redirect(reverse('login'))
		try:
			user = User.objects.get(username = username)
		except User.DoesNotExist:
			user = User(username = username)
			user.set_password(password)
			#user.set_password(password)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			login(request, user)
			return redirect(reverse("home"))
	if(user is not None):
		login(request, user)
		return redirect(reverse("home"))
	return redirect(reverse('login'))