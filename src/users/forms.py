from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    email = forms.EmailField(
        # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/262.
        widget=forms.EmailInput(attrs={"placeholder": _("Email address")})
    )
