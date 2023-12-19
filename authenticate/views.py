from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import View

from .forms import LoginForm


class AuthenticationView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = LoginForm


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
