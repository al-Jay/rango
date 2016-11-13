from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Django saya hi!")

def about(request):
    return HttpResponse("This is the about page")
