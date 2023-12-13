from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class CustomUserRegisterForm(UserCreationForm):
    # Customize the password label
    password1 = forms.CharField(
        label=_("سریال شناسنامه"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("سریال شناسنامه را وارد کنید."),
        min_length=6
    )
    password2 = forms.CharField(
        label=_("تایید سریال شناسنامه"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("برای تایید، سریال شناسنامه را دوباره وارد کنید."),
        min_length=6
    )
    first_name = forms.CharField(label='نام', help_text='نام کاربر را وارد کنید.', max_length=84)
    last_name = forms.CharField(label='نام خانوادگی', help_text='نام خانوادگی کاربر را وارد کنید.', max_length=84)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name')
        help_texts = {'username': 'کدملی 10 رقمی کاربر را وارد کنید.'}
        error_messages = {'password_mismatch': 'سریال شناسنامه و تکرار آن تطابق ندارند.'}
