from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login
# from django.views.generic import View
from django.views.generic import TemplateView

from userprofiles.forms import UserCreationEmailForm, EmailAuthenticationForm


def signup(req):
    form = UserCreationEmailForm(req.POST or None)

    if form.is_valid():
        form.save()

    return render(req, 'signup.html', {'form': form})


def signin(req):
    form = EmailAuthenticationForm(req.POST or None)

    if form.is_valid():
        login(req, form.get_user())

    return render(req, 'signin.html', {'form': form})


# class LoginView(View):

# 	def get(self, req, *args, **kwargs):
# 		return HttpResponse('LoginView !!!')

class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        is_auth = False
        name = None

        if self.request.user.is_authenticated():
            is_auth = True
            name = self.request.user.username

        data = {
            'is_auth': is_auth,
            'name': name
        }

        context.update(data)

        return context


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            context.update({'userprofile': self.get_userprofile()})

        return context

    def get_userprofile(self):
        return self.request.user.userprofile
