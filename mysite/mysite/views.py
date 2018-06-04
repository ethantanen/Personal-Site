from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from static.python_programs import gcd as _gcd
from static.python_programs import prime_factorization as _pf
from django.views.decorators.csrf import csrf_exempt


def home(request):
	return render(request,'home.html',{})

def resume(request):
	return render(request,'resume.html',{})

def projects(request):
	return render(request,'projects.html',{})

@csrf_exempt
def gcd(request):

	a = int(request.POST["a"])
	b = int(request.POST["b"])

	return HttpResponse(_gcd.gcd(a,b))

@csrf_exempt
def prime_factors(request):

	a = int(request.POST["a"])
	p = str(_pf.prime_factors(a))


	return HttpResponse(p)
