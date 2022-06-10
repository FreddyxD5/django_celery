from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django_celery import settings
import time

@shared_task
def send_emails_users():
    asunto = 'Test message'
    message = 'Holitas de mar from Peru, CELERY, RABBITMQ and Django'
    users = User.objects.all()      
    for user in users:                
        time.sleep(1)
        send_mail(
        asunto, message,
        settings.EMAIL_HOST_USER,        
        [user.email],
        fail_silently=False,
        )
        print(f'{user} se envio el correo correctamente.')
    return f'{user} se envio el correo correctamente.'

