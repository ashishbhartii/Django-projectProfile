from django import forms
from django.forms import ModelForm
from projectProfileApp.models import Contact,unregisteredContact

class updateContact(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class updateUnregisteredcontact(ModelForm):
    class Meta:
        model = unregisteredContact
        fields = '__all__'

class TestForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    your_contact = forms.NumberInput()


