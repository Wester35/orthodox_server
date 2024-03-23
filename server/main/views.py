from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the orthodox server!</h1>")


def auth(request):
    return render(request, 'main/sign_in.html')


def register(request):
    return render(request, 'main/sign_up.html')

