from django.db import models
from django.contrib.auth.models import User
from datetime import datetime   
# Create your models here.


class Refueling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    price_per_liter = models.FloatField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    location = models.CharField(null=True, blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
