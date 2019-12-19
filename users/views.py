from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import UsernameEmailPasswordForm, EmailUsernameUpdate, AvatarUploadForm 

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
			messages.success(request, f'You are now registered. Please log in to continue')
			return redirect('login')

	else:
	    form = UsernameEmailPasswordForm()

	return render(request, 'users/register.html', {'form': form})

@login_required
def account(request):
	"""
	Allows user to update their profile information
	such as username and email
	"""
	if request.method == 'POST':
		form = EmailUsernameUpdate(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, f'You have now updated your account details')
			return redirect('account')

	else:
		form = EmailUsernameUpdate(instance=request.user)

	return render(request, 'users/account.html', {'form': form})

@login_required
def avatar_upload(request):
	user = request.user
	instance = get_object_or_404(UserProfile, user=user)
	if request.method == 'POST':
		form = AvatarUploadForm(request.POST, request.FILES,
			instance=instance)
		if form.is_valid():
			form.save()
			return redirect('/')
	form = AvatarUploadForm()

	return render(request, 'users/account.html', {'form': form})



