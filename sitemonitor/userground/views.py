from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def welcome_user(request):
  return HttpResponse("Welcome To User Ground")
