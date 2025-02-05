from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sukku(request):
    return HttpResponse('Sukku is a Playboy')