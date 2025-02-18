


# Create your models here.
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_pass = models.CharField(max_length=100)
    user_blood = models.CharField(max_length=3)
    user_phone = models.CharField(max_length=15)
    user_address = models.TextField()

    def __str__(self):
        return self.user_name



class Worker(models.Model):
    worker_name = models.CharField(max_length=100)
    worker_email = models.EmailField(max_length=100)
    worker_pass = models.CharField(max_length=100)
    worker_phone = models.CharField(max_length=15)
    worker_dob = models.DateField()
    worker_blood = models.CharField(max_length=3)
    worker_address = models.TextField()

    def __str__(self):
        return self.worker_name
    




class Service(models.Model):
    service_name = models.CharField(max_length=100)
    service_desc = models.TextField()
    service_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name





