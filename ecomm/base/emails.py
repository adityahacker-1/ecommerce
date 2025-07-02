from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email, email_token):
    subject = "Your account needs to be activated"
    email_from = settings.EMAIL_HOST_USER
    message = f"Hi, \n\nPlease click on the link below to activate your account: http://127.0.0.1:8000/accounts/activate/{email_token}\n\nThank you!"
    
    send_mail(subject, message, email_from, [email])