from django.shortcuts import render

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from zmain.models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from gymm.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
import requests
import json
URL = "http://18.205.215.155:8000/contactapi/"
def Home(request):
    return render(request, 'frontend/index.html')

def ABOUT(request):
    return render(request, 'frontend/about.html')

def CONTACT(request):
    if request.method == "POST":
        f = request.POST
        mes = f['message']
        nam = f['name']
        ema = f['email']
        sub = f['subject']
        data={'name':nam,'subject':sub,'Email':ema,'Address':mes}
        headers={'content-type':'application/json'}
        requests.post(url=URL,data=json.dumps(data),headers=headers)
    return render(request, 'frontend/contact.html')

def GALLERY(request):
    return render(request, 'frontend/gallery.html')

def PRODUCT(request):
    return render(request, 'frontend/product.html')

def SERVICES(request):
    return render(request, 'frontend/services.html')

def BLOG(request):
    return render(request, 'frontend/blog.html')

