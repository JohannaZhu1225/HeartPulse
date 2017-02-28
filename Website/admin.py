from django.contrib import admin

# Register your models here.

from .models import EmailAddress, HeartRate

admin.site.register(EmailAddress)

admin.site.register(HeartRate)