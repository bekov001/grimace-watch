from django.db import models
 
class History(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    address = models.CharField(max_length=43)
    total = models.FloatField()

class Tokens(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()