from django import forms
from django.utils.translation import ugettext_lazy as _

from applications.models import Application


class ScholarshipApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("background", "reason_to_attend")
        labels = {
            "background": _("Tell us a little bit about yourself"),
            "reason_to_attend": _("Why are you interested in attending PyGotham?"),
        }
