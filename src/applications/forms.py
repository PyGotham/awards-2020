from __future__ import annotations

from typing import Any, Dict

from django import forms
from django.utils.translation import gettext_lazy as _

from applications.models import Application


# pyre-fixme[13]: This whole class hierarchy needs to be cleaned up.
class ApplicationForm(forms.ModelForm):
    type: Application.Type


class FinancialAidApplicationForm(ApplicationForm):
    type = Application.Type.FINANCIAL_AID

    travel_requested = forms.BooleanField(
        label=_("Do you need assistance with travel?"), required=False,
    )

    class Meta:
        model = Application
        fields = (
            "background",
            "reason_to_attend",
            "travel_requested",
            "travel_amount",
            "lodging_requested",
        )
        labels = {
            "background": _("Tell us a little bit more about yourself"),
            "lodging_requested": _("Do you need assistance with lodging?"),
            "reason_to_attend": _("Why are you interested in attending PyGotham?"),
            "travel_amount": _("What is the estimated cost (USD)?"),
        }
        widgets = {
            "lodging_requested": forms.CheckboxInput(),
        }

    def clean(self) -> Dict[str, Any]:
        cleaned_data = super().clean()

        travel_amount = cleaned_data.get("travel_amount") or 0
        if travel_amount < 0:
            raise forms.ValidationError(
                {"travel_amount": _("Your estimated travel costs cannot be negative.")}
            )

        travel_requested = cleaned_data.get("travel_requested")
        if travel_requested:
            if not travel_amount:
                raise forms.ValidationError(
                    {
                        "travel_amount": _(
                            "Your estimated travel costs must be greater than $0.00."
                        )
                    }
                )
        elif travel_amount:
            msg = _(
                "You must request travel assistance before providing an estimated cost."
            )
            raise forms.ValidationError({"travel_requested": msg})

        return cleaned_data

    def clean_lodging_requested(self) -> bool:
        return bool(self.cleaned_data.get("lodging_requested"))


class ScholarshipApplicationForm(ApplicationForm):
    type = Application.Type.SCHOLARSHIP

    class Meta:
        model = Application
        fields = ("background", "reason_to_attend")
        labels = {
            "background": _("Tell us a little bit about yourself"),
            "reason_to_attend": _("Why are you interested in attending PyGotham?"),
        }


APPLICATION_FORM_TYPES = {
    Application.Type.FINANCIAL_AID: FinancialAidApplicationForm,
    Application.Type.SCHOLARSHIP: ScholarshipApplicationForm,
}
