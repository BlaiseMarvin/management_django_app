from django.db import models
import os
import random
import string

class InternProfile(models.Model):
    def profile_photo_upload_to(self,instance=None):
        if instance:
            random_text=''.join(random.sample(string.ascii_lowercase, 10))
            return os.path.join('profile_photos',f'{self.firstname} - {self.lastname}',random_text,instance)
        return None
    profile_photo=models.ImageField(upload_to=profile_photo_upload_to,null=True)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField()
    age=models.IntegerField()
    university=models.CharField(max_length=255)