from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date_of_birthday = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=30)
    occupation = models.CharField(max_length=200)
    status = models.CharField(max_length=30)
