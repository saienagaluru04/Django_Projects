from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def djforms(request):
    ESTFO = StudentForm()
    d = {'ESTFO':ESTFO}

    if request.method == 'POST':
        STFOWD  = StudentForm(request.POST)
        if STFOWD.is_valid():
            return HttpResponse(str(STFOWD.cleaned_data))
        else:
            return HttpResponse('Invalid data.')
    return render(request,'djforms.html',d)