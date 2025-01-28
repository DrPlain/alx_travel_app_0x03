from celery import shared_task
from django.core.mail import send_mail
from alx_travel_app import settings


@shared_task
def send_booking_confirmation_email(recipient_email, booking_details):
    subject = "Booking Confirmation"
    message = f"Dear Customer,\n\nYour booking was successful. Details:\n\n{booking_details}\n\nThank you!"
    sender_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, sender_email, [
              recipient_email], fail_silently=False)
    return "Email sent successfully."


@shared_task
def add(a, b):
    return a+b
