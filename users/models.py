from __future__ import annotations

from typing import List

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import CIEmailField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str) -> User:
        user = User(email=email)
        user.save()
        return user

    def create_superuser(self, email: str, password: str) -> User:
        user = User(email=email, is_staff=True)
        user.save()
        return user


class User(AbstractBaseUser):
    email = CIEmailField(_("email address"), unique=True)
    # Blank passwords are allowed since we only allow applicants to use
    # magic links to log in.
    password = models.CharField(_("password"), max_length=128, blank=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(_("user can access the admin"), default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # type: List[str]

    objects = UserManager()

    is_active = True

    def __str__(self) -> str:
        username, domain = self.email.split("@", 1)

        # Hide the characters in the username other than the first one.
        return f"{username[0]}{'*' * (len(username) - 1)}@{domain}"

    # These methods are required by the Django admin.
    def has_module_perms(self, package_name: str) -> bool:
        return self.is_staff

    def has_perm(self, perm: str, object: object = None) -> bool:
        return self.is_staff
