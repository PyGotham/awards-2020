from django.urls import path

from applications.forms import (
    FinancialAidApplicationForm,
    ScholarshipApplicationForm,
)
from applications.views import apply, view

app_name = "applications"

urlpatterns = [
    path("edit/<int:pk>", apply, name="edit"),
    path(
        "financial-aid",
        apply,
        {"form_type": FinancialAidApplicationForm},
        name="financial_aid",
    ),
    path(
        "ticket", apply, {"form_type": ScholarshipApplicationForm}, name="scholarship"
    ),
    path("view/<int:pk>", view, name="view"),
]
