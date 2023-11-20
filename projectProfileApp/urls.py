from django.contrib import admin
from django.urls import path, include
from projectProfileApp import views


admin.site.site_header = "Developer Ashish"
admin.site.site_title = "Welcome to Ashish Dashboard"
admin.site.index_title = "Welcome to Ashish’s Admin Portral"

urlpatterns = [
    path('',views.base, name='base'),
    path('home',views.home, name='home'),
    path('explore',views.explore, name='explore'),
    path('signin/',views.signin, name='signin'),
    path('invalidpassword',views.invalidpassword, name='invalidpassword'),
    path('login',views.login, name='login'),
    path('invalidcredentials',views.invalidcredentials, name='invalidcredentials'),
    path('projects',views.projects, name='projects'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('basecontact',views.basecontact, name='basecontact'),
    path('testform',views.testform, name='testform'),
    path('unregisteredcontacts',views.unregisteredcontacts, name='unregisteredcontacts'),
    path('registeredcontacts',views.registeredcontacts, name='registeredcontacts'),
    path('deleteUR/<int:id>/',views.deleteUR, name='deleteUR'),
    path('deleteR/<int:id>/',views.deleteR, name='deleteR'),
    path('updateUR/<int:id>/',views.updateUR, name='updateUR'),
    # path('unregisteredcontacts/<int:id>/update', views.updateUR, name='update_ur'),
    path('updateR/<int:id>/',views.updateR, name='updateR'),
]