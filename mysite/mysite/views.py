from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

from static.python_programs import gcd as _gcd
from static.python_programs import prime_factorization as _pf

def home(request):
	return render(request,'home.html',{})

def resume(request):
	return render(request,'resume.html',{})

def projects(request):
	return render(request,'projects.html',{})

@csrf_exempt
def email(request):

	name = request.POST.get("name","john doe")
	email = request.POST.get("email","yougotgot@gotgot.com")
	message = request.POST.get("message","you got got")

	template = get_template('contact_template.txt')
	context = {
		'contact_name': name,
		'contact_email': email,
		'form_content': message
	}

	content = template.render(context)

	email = EmailMessage(
		"New contact form Submission",
		content,
		"Your website" + ' ',
		["ethantanen@yahoo.com"],
		headers = {'Reply-To': email}
	)

	email.send()

	return render(request,'home.html',{})



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
