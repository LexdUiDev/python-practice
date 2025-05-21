from django.core.mail import EmailMessage
from django.conf import settings

def send_email(data):
    to= data.get('to')
    subject= data.get('subject')
    body= data.get('body')
    from_email= settings.EMAIL_HOST_USER
    email= EmailMessage(subject= subject, body= body, from_email= from_email, to=[to])