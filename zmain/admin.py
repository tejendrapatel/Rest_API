from django.contrib import admin
from .models import contactss

@admin.register(contactss)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject','Email','Address']
