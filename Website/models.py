from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EmailAddress(models.Model):
    email = models.CharField(max_length=500, default="")
    display_name = models.CharField(max_length=500, default="")
    address = models.CharField(max_length=500, default="")
    phone_number = models.CharField(max_length=500, default="")
    comments = models.CharField(max_length=500, default="")
	
    def __str__(self):
        return self.email
	
class HeartRate(models.Model):
    user = models.ForeignKey(EmailAddress, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    timeSince1970 = models.BigIntegerField(default=0)
	
    def __str__(self):
        return str(self.rate)