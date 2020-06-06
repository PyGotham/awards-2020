from __future__ import annotations

from typing import Type

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from applications.forms import APPLICATION_FORM_TYPES, ApplicationForm
from applications.models import Application


@login_required
def apply(request: HttpRequest, form_type: Type[ApplicationForm]) -> HttpResponse:
    if request.method == "POST":
        application = Application(applicant=request.user, type=form_type.type)
        form = form_type(request.POST, instance=application)
        if form.is_valid():

            form.save()

            return HttpResponse("Thank you for your application")
    else:
        form = form_type()

    return render(request, "applications/form.html", {"form": form})


@login_required
def view(request: HttpRequest, pk: int) -> HttpResponse:
    application = get_object_or_404(Application, pk=pk, applicant=request.user)
    form_type = APPLICATION_FORM_TYPES[application.type]
    form = form_type(instance=application)
    return render(request, "applications/view.html", {"form": form})
