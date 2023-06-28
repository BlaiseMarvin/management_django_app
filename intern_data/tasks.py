from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_profile_created_mail(firstname,lastname,email):
    send_mail('Account Created',f'Hello {firstname} {lastname}, your account has been created successfully','bmrusoke@gmail.com',[email])
