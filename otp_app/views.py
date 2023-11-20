from django.http import HttpResponse
from django.shortcuts import render, redirect
from  otp_app.forms import otpform

def otp(request):
    fn = otpform()
    data = {'form':fn}
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        data ={
            'form':fn
        }
        return
    return render()