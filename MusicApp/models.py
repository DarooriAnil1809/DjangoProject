from django.db import models

# Create your models here.
class Musician(models.Model):

    def __str__(self):
        return self.first_name

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=300)
    instrument_name = models.CharField(max_length=100)

