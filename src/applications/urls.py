from django.urls import path

from applications.views import (
    FinancialAidApplicationFormView,
    ScholarshipApplicationFormView,
    view,
)

app_name = "applications"

urlpatterns = [
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path(
        "financial-aid",
        FinancialAidApplicationFormView.as_view(),
        name="financial_aid",
    ),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path(
        "financial-aid/<int:pk>",
        FinancialAidApplicationFormView.as_view(),
        name="edit_financial_aid",
    ),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("ticket", ScholarshipApplicationFormView.as_view(), name="scholarship",),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path(
        "ticket/<int:pk>",
        ScholarshipApplicationFormView.as_view(),
        name="edit_scholarship",
    ),
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    path("view/<int:pk>", view, name="view"),
]
