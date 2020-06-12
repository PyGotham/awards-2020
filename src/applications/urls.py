from django.urls import path

from applications.forms import (
    FinancialAidApplicationForm,
    ScholarshipApplicationForm,
)
from applications.views import apply, view

app_name = "applications"

urlpatterns = [
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("edit/<int:pk>", apply, name="edit"),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path(
        "financial-aid",
        apply,
        {"form_type": FinancialAidApplicationForm},
        name="financial_aid",
    ),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path(
        "ticket", apply, {"form_type": ScholarshipApplicationForm}, name="scholarship"
    ),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("view/<int:pk>", view, name="view"),
]
