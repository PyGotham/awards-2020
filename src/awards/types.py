from __future__ import annotations

from typing import Protocol, Type

from django.contrib.auth.models import AbstractBaseUser
from django.http import HttpRequest


# user isn't actually part of HttpRequest; it gets added by
# django.contrib.auth.middleware.AuthenticationMiddleware. Using this
# class instead will allow code that relies on request.user to pass the
# type checker.
class HttpRequestWithUser(HttpRequest, Protocol):
    """A wrapper around HttpRequest that includes ``user``."""

    user: Type[AbstractBaseUser]
