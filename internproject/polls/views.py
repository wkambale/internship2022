from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# funcName(param1, param2):

def index(request):
	return HttpResponse("Hello, World")
