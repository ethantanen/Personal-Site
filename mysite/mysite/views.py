from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request,'home.html',{})

def resume(request):
	return render(request,'resume.html',{})

def projects(request):
	return render(request,'projects.html',{})
