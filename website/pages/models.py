from django.db import models
from django.forms import ModelForm
from datetime import datetime


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date_of_birthday = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=30)
    occupation = models.CharField(max_length=200)
    status = models.CharField(max_length=30)

    quote = models.TextField(blank=True, db_index=True)
    biography = models.TextField(blank=True, db_index=True)
    pic = models.ImageField(upload_to='pages/media')


    def __str__(self):
        return self.name


class Contact_Info(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    topic = models.CharField(max_length=30)
    message = models.TextField(blank=True)
    response = models.BooleanField()
    date_submitted = models.DateTimeField(default=datetime.now, blank=True)


    
