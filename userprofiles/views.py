from django.shortcuts import render
from django.contrib.auth import login

from userprofiles.forms import UserCreationEmailForm, EmailAuthenticationForm

def signup(req):
	form = UserCreationEmailForm(req.POST or None)

	if form.is_valid():
		form.save()

	return render(req, 'signup.html', { 'form': form })

def signin(req):
	form = EmailAuthenticationForm(req.POST or None)

	if form.is_valid():
		login(req, form.get_user())
		
	return render(req, 'signin.html', {'form': form})