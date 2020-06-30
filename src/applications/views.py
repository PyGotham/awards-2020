from __future__ import annotations

from typing import Any, ClassVar, Dict, Optional, Type

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_GET
from django.views.generic.detail import DetailView

from applications.forms import (
    APPLICATION_FORM_TYPES,
    ApplicationForm,
    FinancialAidApplicationForm,
    ScholarshipApplicationForm,
)
from applications.models import Application

# pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
User = get_user_model()


class ApplicationDetailView(DetailView):
    model = Application
    template_name = "applications/views.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        application = context["object"]
        context["form"] = APPLICATION_FORM_TYPES[application.type](instance=application)
        return context

    def get_object(self) -> Application:
        return self.model.objects.get(pk=self.kwargs["pk"], applicant=self.request.user)


@method_decorator(login_required, name="dispatch")
class _ApplicationFormView(View):
    form_class: ClassVar[Type[ApplicationForm]] = ApplicationForm
    template_name = "applications/form.html"

    # pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    def _get_application(self, user: User, pk: Optional[int] = None) -> Application:
        if pk is None:
            application = Application(applicant=user, type=self.form_class.type)
        else:
            application = get_object_or_404(Application, pk=pk, applicant=user)

        return application

    def get(self, request: HttpRequest, pk: Optional[int] = None) -> HttpResponse:
        form = self.form_class(instance=self._get_application(user=request.user, pk=pk))
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest, pk: Optional[int] = None) -> HttpResponse:
        form = self.form_class(
            request.POST, instance=self._get_application(user=request.user, pk=pk)
        )
        if form.is_valid():
            form.save()

            if pk:
                msg = "Your application has been updated"
            else:
                msg = "Thank you for your application"
            return HttpResponse(msg)

        return render(request, self.template_name, {"form": form})


class FinancialAidApplicationFormView(_ApplicationFormView):
    form_class = FinancialAidApplicationForm


class ScholarshipApplicationFormView(_ApplicationFormView):
    form_class = ScholarshipApplicationForm


@login_required
@require_GET
def view(request: HttpRequest, pk: int) -> HttpResponse:
    application = get_object_or_404(Application, pk=pk, applicant=request.user)
    form_type = APPLICATION_FORM_TYPES[application.type]
    form = form_type(instance=application)
    return render(request, "applications/view.html", {"form": form})
