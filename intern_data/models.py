from django.db import models

class InternProfile(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField()
    age=models.IntegerField()
    university=models.CharField(max_length=255)