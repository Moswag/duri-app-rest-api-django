from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


    def __self__(self):
        return self.name