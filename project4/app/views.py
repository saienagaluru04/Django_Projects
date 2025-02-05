from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def valentine(request):
    return render(request,'valentine.html')


def kumar(request):
    return HttpResponse('Hi this is Sai kumar Enagaluru')



# def home(request):
#     return render(request,'home.html')