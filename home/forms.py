from django import forms

class ContactForm(forms.Form):
	""" Contact form for users to send messages"""

	name = forms.CharField()
	email = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)

class Meta:
	fields = [
		'name',
		'email',
		'message',
	]