from django.shortcuts import render
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm

def index(request):

	return render(request, 'home/index.html')

def about(request):

	return render(request, 'home/about.html')

def contact(request):

	contact_form = ContactForm()
	emailjs_id = settings.EMAILJS_ID

	context = {
		"page": contact,
		"form": contact_form,
		"emailjs_id": emailjs_id, 
	}

	return render(request, 'home/contact.html', context)

""" credit: https://stackoverflow.com/questions/46542502/django-
how-to-add-a-logout-successful-message-using-the-django-contrib-auth """

# show logout message when user logs out
def show_logout_message(sender, user, request, **kwargs):
	if user_logged_out:
		messages.success(request, 'You have been logged out.')

user_logged_out.connect(show_logout_message)

# show login message when user logs in
def show_login_message(sender, user, request, **kwargs):
	if user_logged_in:
		messages.success(request, 'You are logged in.')

user_logged_in.connect(show_login_message)