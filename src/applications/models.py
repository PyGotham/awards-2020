from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

# pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
User = get_user_model()


class Application(models.Model):
    # pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    class Status(models.TextChoices):
        PENDING = "pending"

    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    applicant = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    background = models.TextField(_("applicant background"))
    reason_to_attend = models.TextField(_("reason the applicant wishes to attend"))
    status = models.CharField(
        max_length=20,
        # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self) -> str:
        return f"Application for {self.applicant}"
