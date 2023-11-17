from django.db import models
 
class History(models.Model):
    address = models.CharField(max_length=43)
    total = models.FloatField()

class Tokens(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()