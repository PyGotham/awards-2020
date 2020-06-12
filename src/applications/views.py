from __future__ import annotations

from typing import Optional, Type

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from applications.forms import APPLICATION_FORM_TYPES, ApplicationForm
from applications.models import Application


@login_required
def apply(
    request: HttpRequest,
    form_type: Optional[Type[ApplicationForm]] = None,
    pk: Optional[int] = None,
) -> HttpResponse:
    # If no form_type is provided, we're editing an existing
    # application. Use it's primary key to look it up and determine
    # which form type to use.
    if form_type is None:
        if pk is None:
            # If neither value was provided, we shouldn't be here.
            raise Http404()

        application = get_object_or_404(Application, pk=pk, applicant=request.user)
        form_type = APPLICATION_FORM_TYPES[application.type]
    else:
        application = Application(applicant=request.user, type=form_type.type)

    if request.method == "POST":
        form = form_type(request.POST, instance=application)
        if form.is_valid():
            form.save()

            if pk:
                msg = "Your application has been updated"
            else:
                msg = "Thank you for your application"
            return HttpResponse(msg)
    else:
        form = form_type(instance=application)

    return render(request, "applications/form.html", {"form": form})


@login_required
def view(request: HttpRequest, pk: int) -> HttpResponse:
    application = get_object_or_404(Application, pk=pk, applicant=request.user)
    form_type = APPLICATION_FORM_TYPES[application.type]
    form = form_type(instance=application)
    return render(request, "applications/view.html", {"form": form})
