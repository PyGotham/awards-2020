from __future__ import annotations

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from sesame.utils import get_query_string, get_user

from applications.models import Application
from users.forms import LoginForm


def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
        User = get_user_model()

        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            user, _ = User.objects.get_or_create(email=email)

            qs = get_query_string(user)
            login_url = request.build_absolute_uri(reverse("magic-login")) + qs

            message = f'<a href="{login_url}">{login_url}</a>'
            send_mail(
                "PyGotham Financial Aid and Scholarship Login",
                login_url,
                settings.EMAIL_SENDER,
                [user.email],
                html_message=message,
            )

            # TODO: This should probably be a redirect instead.
            return HttpResponse("email sent")
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})


def magic_login(request: HttpRequest) -> HttpResponse:
    user = get_user(request)
    if user:
        return redirect("users:profile")
    return redirect("oops")


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    applications = Application.objects.filter(applicant=request.user)
    return render(request, "users/profile.html", {"applications": applications})
