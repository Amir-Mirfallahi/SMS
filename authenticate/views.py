from django.contrib.auth.views import LoginView
from .forms import LoginForm


class AuthenticationView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = LoginForm
    
