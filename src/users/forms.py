from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": _("Email address")})
    )
