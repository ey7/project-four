from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from cloudinary.forms import CloudinaryFileField
from .models import UserProfile

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

class AvatarUploadForm(forms.ModelForm):
	avatar = CloudinaryFileField(
		options = {
		'crop': 'thumb',
		'width': '200',
		'height': '200',
		'folder': 'avatars'
		}
	)
	class Meta: 
		model = UserProfile
		fields = ['avatar']







