from django.db import models

# Create your models here.
class Logistics(models.Model):

    def __str__(self):
        return self.Account_No

    Request_No = models.BigIntegerField()
    Request_Name = models.CharField(max_length=200)
    Account_No = models.CharField(max_length=200)