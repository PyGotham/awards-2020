from django import forms
from django.utils.translation import gettext_lazy as _

from applications.models import Application


# pyre-fixme[13]: This whole class hierarchy needs to be cleaned up.
class ApplicationForm(forms.ModelForm):
    type: Application.Type


class FinancialAidApplicationForm(ApplicationForm):
    type = Application.Type.FINANCIAL_AID

    class Meta:
        model = Application
        fields = ("background", "reason_to_attend")
        labels = {
            # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/262.
            "background": _("Tell us a little bit more about yourself"),
            # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/262.
            "reason_to_attend": _("Why are you interested in attending PyGotham?"),
        }


class ScholarshipApplicationForm(ApplicationForm):
    type = Application.Type.SCHOLARSHIP

    class Meta:
        model = Application
        fields = ("background", "reason_to_attend")
        labels = {
            # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/262.
            "background": _("Tell us a little bit about yourself"),
            # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/262.
            "reason_to_attend": _("Why are you interested in attending PyGotham?"),
        }
