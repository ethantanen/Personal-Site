from django.shortcuts import render
from django.http import HttpResponse

def test(request):
	return render(request,'template.html',{})

def home(request):
	return render(request,'home.html',{})

def resume(request):
	return render(request,'resume.html',{})

def projects(request):
	return render(request,'projects.html',{})
