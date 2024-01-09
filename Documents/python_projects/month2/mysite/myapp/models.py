from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=50)
    capacity = models.IntegerField(blank=True, null=True)
    date_of_manufacture = models.DateField(auto_now_add=True)
    horse_power = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(default=0,max_digits=8, decimal_places=2, blank=True)
    class Meta:
        ordering = ["-id"]