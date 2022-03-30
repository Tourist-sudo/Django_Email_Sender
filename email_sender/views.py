from email import message
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse


def index(request):
    message = loader.render_to_string(
        'email_sender/message.html', {'name': 'Shivam', 'body': 'You have received this email!'})
    send_mail('Congratulations!', 'You have recieved this email!',
              'sender_mail@gmail.com', ['receiver_email@gmail.com'], html_message=message, fail_silently=False)
    return HttpResponse("MAIL SENT!!")
