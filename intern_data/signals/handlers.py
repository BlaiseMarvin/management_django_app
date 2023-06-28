from django.dispatch import receiver
from django.db.models.signals import post_save
from ..models import InternProfile


@receiver(post_save,sender=InternProfile)
def send_email_after_profile_save(sender,**kwargs):
    if kwargs['created']:
        firstname=kwargs['instance'].firstname
        lastname=kwargs['instance'].lastname
        email=kwargs['instance'].email

        