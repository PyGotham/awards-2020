from __future__ import annotations

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from applications.forms import ScholarshipApplicationForm
from applications.models import Application


@login_required
def scholarship(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        application = Application(applicant=request.user)
        form = ScholarshipApplicationForm(request.POST, instance=application)
        if form.is_valid():

            form.save()

            return HttpResponse("Thank you for your application")
    else:
        form = ScholarshipApplicationForm()

    return render(request, "applications/scholarship.html", {"form": form})
