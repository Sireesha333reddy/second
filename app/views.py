from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
def siri(request):
    return HttpResponse('hey siri')
