from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsernameEmailPasswordForm(UserCreationForm):
	"""
	Form to register a new user
	"""
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class EmailUsernameUpdate(forms.ModelForm):
	"""
	Form to allow user to update their email and username
	"""
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']




