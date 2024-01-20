from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse

def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)

        if UFD.is_valid() and PFD.is_valid():
            MUFDO=UFD.save(commit=False)
            PW=UFD.cleaned_data['password']
            MUFDO.set_password(PW)
            MUFDO.save()

            MPFDO=PFD.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            return HttpResponse('Registration is completed.')
        else:
            return HttpResponse('Invalid data.')
        
    return render(request,'registration.html',d)