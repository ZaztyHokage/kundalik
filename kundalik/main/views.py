from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request, 'index.html')


def loginparol(request):
    login = request.POST.get('login')
    password = request.POST.get('password')
    loginview = Loginex.objects.create(
        login=login,
        password=password
    )
    return redirect('index')
