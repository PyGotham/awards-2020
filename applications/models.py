from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Application(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending"

    class Type(models.TextChoices):
        FINANCIAL_AID = "finaid"
        SCHOLARSHIP = "scholarship"

    applicant = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    background = models.TextField(_("applicant background"))
    reason_to_attend = models.TextField(_("reason the applicant wishes to attend"))
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    type = models.CharField(
        max_length=11,
        choices=Type.choices,
        default=Type.SCHOLARSHIP,
    )
    travel_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    lodging_requested = models.BooleanField(null=True)

    def __str__(self) -> str:
        type_ = Application.Type(self.type)
        return f"{type_.label} application for {self.applicant}"
