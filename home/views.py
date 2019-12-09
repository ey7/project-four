from django.shortcuts import render
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages

def index(request):

	return render(request, 'home/index.html')

def about(request):

	return render(request, 'home/about.html')

""" credit: https://stackoverflow.com/questions/46542502/django-how-to-add-a-logout-successful
-message-using-the-django-contrib-auth"""

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