from __future__ import annotations

from typing import Type

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.forms import ApplicationForm
from applications.models import Application


@login_required
def apply(request: HttpRequest, form_type: Type[ApplicationForm]) -> HttpResponse:
    print(form_type)
    if request.method == "POST":
        application = Application(applicant=request.user, type=form_type.type)
        form = form_type(request.POST, instance=application)
        if form.is_valid():

            form.save()

            return HttpResponse("Thank you for your application")
    else:
        form = form_type()

    return render(request, "applications/form.html", {"form": form})
