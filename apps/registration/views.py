# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
import bcrypt


def index(request):
	all_users=User.objects.all()
	context = {
		'all': all_users
	}
	print 'sup'
	return render(request, 'registration/index.html', context)
def new(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):	
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		
		if request.method=="POST":
			print request.POST
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			email = request.POST['email']
			password = request.POST['password']
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

			user=User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
			print user.id
			return redirect("/success/" + str(user.id))
		else:
			return redirect('/')
def login(request):
	loginerrors= User.objects.loginval(request.POST)
	all_users=User.objects.all()
	context = {
		'all': all_users
	}
	if len(loginerrors):
		for tag, error in loginerrors.iteritems():
			messages.error(request, error, extra_tags=tag)
			return redirect('/')
	else:
		if request.method=="POST":
			user= User.objects.get(email = request.POST['email'])
			print request.POST
			email=request.POST['email']
			password=request.POST['password']
			# if bcrypt.checkpw(password.encode(), hashed.encode()) == hashed:
			return redirect("/success/" + str(user.id))
		else:
			return redirect('/')



	


def success(request, id):
	user=User.objects.get(id=id)
	context = {
		'all': user
	}
	
	return render(request, "registration/success.html", context)

	
# Create your views here.
