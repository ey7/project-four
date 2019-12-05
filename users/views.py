from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import UsernameEmailPasswordForm 

def register(request):
	"""
	Allows users to register for an account.
	Once form is validated, redirects users to the login page
	"""
	if request.method == 'POST':
		form = UsernameEmailPasswordForm(request.POST)
		if form_is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('login')

	else:
	    form = UsernameEmailPasswordForm()
	    return render(request, 'users/register.html')
