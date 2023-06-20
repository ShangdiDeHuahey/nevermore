from django.contrib import admin
from .models import ContactModel

# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time',)

admin.site.register(ContactModel, MyModelAdmin)