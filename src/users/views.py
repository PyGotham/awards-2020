from __future__ import annotations

from awards.types import HttpRequestWithUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from sesame.utils import get_query_string, get_user


def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        User = get_user_model()

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

        return HttpResponse("email sent")

    return render(request, "users/login.html")


def magic_login(request: HttpRequest) -> HttpResponse:
    user = get_user(request)
    if user:
        return redirect("profile")
    return redirect("oops")


@login_required
def profile(request: HttpRequestWithUser) -> HttpResponse:
    return HttpResponse(f"Hello {request.user}")
