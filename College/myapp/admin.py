from django.contrib import admin
from myapp.models import Contact, signtbl, admintbl

# Register your models here.
admin.site.register(Contact)
admin.site.register(signtbl)
admin.site.register(admintbl)


