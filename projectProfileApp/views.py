from django.shortcuts import render,HttpResponse,redirect
from projectProfileApp import models 
from django.contrib.auth.models import User
# This model being imported in views will help us to perform operations on the database
from projectProfileApp.models import Contact
# Here we are importing the Model Class to save the data in the contact function
from projectProfileApp.models import unregisteredContact,Contact
from projectProfileApp.models import signinData, Name
# Create your views here.
from django.contrib.auth import authenticate
# to import authenticate function to validate user
from django.contrib.auth import login as auth_login
# to import login_rquired decorator to protect the pages from being accessed or viewd directly
from django.contrib.auth.decorators import login_required
# to import forms
from projectProfileApp.forms import TestForm
# to import two newly created model forms to up[date]
from projectProfileApp.forms import updateContact,updateUnregisteredcontact

def base(request):
    return render(request,'base.html')


def explore(request):
    return render(request,'explore.html')

@login_required(login_url="login")
def signin(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        phone=request.POST['phone']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print(fname,lname,uname,email,phone,password1,password2)
        if password1 != password2:
            return render(request,'invalidpassword.html')
        else:
            ins = signinData(fname=fname, lname=lname, uname=uname, email=email, phone=phone)
            ins.save()
            my_user=User.objects.create_user(uname,email,password1)
            my_user.save()
            print(f"First time user {fname} {lname} has been successfully registered")
            return redirect('home')
    return render(request,'signin.html')

@login_required(login_url="login")
def invalidpassword(request):
    return render(request,'invalidpassword.html')

def login(request):
    if request.method=='POST':
        user=authenticate(request,
            username=request.POST['uname'],
             password=request.POST['password1']
        )
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
           return render(request,'invalidcredentials.html') 
    return render(request,'login.html')

@login_required(login_url="login")
def invalidcredentials(request):
    return render(request,'invalidcredentials.html')

@login_required(login_url="login")
def home(request):
    return render(request,'home.html')
    # return HttpResponse("Hi, this is from home.html")

@login_required(login_url="login")
def projects(request):
    return render(request,'projects.html')
    # return HttpResponse("Hi, this is from projects.html")

@login_required(login_url="login")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("Hi, this is from about.html")

@login_required(login_url="login")
def contact(request):
    context ={'success':False}
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,email,phone,desc)
        # Here we are creating the instance to store values inside our Class Contact 
        ins =Contact(name=name, email=email, phone=phone, desc=desc)
        # Here we save the data into the database
        ins.save()
        print("the data has been successfully registered to the database")
        context ={'success':True}
    return render(request,'contact.html',context)
    # return HttpResponse("Hi, this is from contact.html")

def basecontact(request):
    context ={'success':False}
    if request.method=='POST':
        name1=request.POST['name1']
        email1=request.POST['email1']
        phone1=request.POST['phone1']
        desc1=request.POST['desc1']
        print(name1,email1,phone1,desc1)
        # Here we are creating the instance to store values inside our Class Contact 
        ins =unregisteredContact(name1=name1, email1=email1, phone1=phone1, desc1=desc1)
        # Here we save the data into the database
        ins.save()
        print()
        print("the data of UNREGISTERED USER successfully registered to the database")
        print()
        context ={'success':True}
    return render(request,'basecontact.html',context)

def testform(request):
    if request.method=='POST':
        form=TestForm(request.POST)
        if form.is_valid():
            your_name=form.cleaned_data['your_name']
            name_ins= Name.objects.create(name=your_name)
            name_ins.save()
            return HttpResponse(f"Test Name was created which is {your_name} ")
    form = TestForm()
    return render(request,'testform.html', {'form':form})  

@login_required(login_url="login")
def unregisteredcontacts(request):
    allUNRData = unregisteredContact.objects.all()
    context = {'undata' : allUNRData }
    return render(request,'unregisteredcontacts.html',context) 

@login_required(login_url="login")
def registeredcontacts(request):
    allRData = Contact.objects.all()
    context = {'rdata' : allRData }
    return render(request,'registeredcontacts.html',context) 


def deleteUR(request,id):
    deleur = unregisteredContact.objects.get(id=id)
    deleur.delete()
    return redirect('unregisteredcontacts')


def deleteR(request,id):
    deler = Contact.objects.get(id=id)
    deler.delete()
    return redirect('registeredcontacts')

def updateUR(request,id):
    updateur = unregisteredContact.objects.get(id=id)
    
    if request.method == 'POST':
        formur=updateUnregisteredcontact(request.POST,instance=updateur)
        if formur.is_valid():
            formur.save()
            return redirect('unregisteredcontacts')
    else:
        formur = updateUnregisteredcontact(instance=updateur)
    context = {'formur': formur}
    return render(request,'updateUR.html',context)

def updateR(request,id):
    updater = Contact.objects.get(id=id)
    formr = updateContact(instance=updater)
    if request.method == 'POST':
        formr = updateContact(request.POST,instance=updater)

    context = {'formr': formr}
    return render(request,'updateR.html',context)

