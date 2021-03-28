from django.db import models


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
        
    def photo(self):
        return '<img src = "%s">' % (self.pic)

    photo.allow_tags = True
    photo.short_description = 'Photo of Doctor House'

    
