from django.urls import path
from otp_app import views

urlpatterns = [
    path('app', views.otp, name='otp'),
]