from django.contrib import admin
from projectProfileApp.models import Contact
from projectProfileApp.models import signinData
from projectProfileApp.models import unregisteredContact,Name
# Register your models here.
admin.site.register(Contact)
admin.site.register(signinData)
admin.site.register(unregisteredContact)
admin.site.register(Name)