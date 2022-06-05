from django.db import models

# Create your models here.
class Emplo(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=50)
    marks = models.FloatField()
    