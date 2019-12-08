from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import UsernameEmailPasswordForm, EmailUsernameUpdate 

def register(request):
	"""
	Allows users to register for an account.
	Once form is validated, redirects users to the login page
	"""
	if request.method == 'POST':
		form = UsernameEmailPasswordForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('login')

	else:
	    form = UsernameEmailPasswordForm()

	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	"""
	Allows user to update their profile information
	such as username and email
	"""
	if request.method == 'POST':
		form = EmailUsernameUpdate(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
		form = EmailUsernameUpdate(instance=request.user)

	return render(request, 'users/profile.html', {'form': form})


