from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("کدملی"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label=_("سریال شناسنامه"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    error_messages = {
        'invalid_login': _(
            "نام کاربری یا رمز عبور اشتباه است."
        ),
        'inactive': _("این حساب کاربری غیرفعال است."),
    }
