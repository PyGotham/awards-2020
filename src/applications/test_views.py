from __future__ import annotations

from django.contrib.auth import get_user_model
from django.test import Client
from factory.django import DjangoModelFactory
import pytest
from sesame.utils import get_query_string

from applications.models import Application


# pyre-ignore[13]: Investigate type stubs for factory-boy.
class ApplicationFactory(DjangoModelFactory):
    class Meta:
        model = Application

    id: int
    type = Application.Type.SCHOLARSHIP


class UserFactory(DjangoModelFactory):
    class Meta:
        # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
        model = get_user_model()
        django_get_or_create = ("email",)

    email = "user@example.org"


@pytest.mark.django_db
# pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
def test_user_can_view_their_application(client: Client) -> None:
    user = UserFactory()
    qs = get_query_string(user)
    client.get(f"/login/magic{qs}")

    # pyre-ignore[28]: Investigate type stubs for factory-boy.
    application = ApplicationFactory(applicant=user)

    response = client.get(f"/apply/view/{application.id}")
    assert response.status_code == 200


@pytest.mark.django_db
# pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
def test_user_cant_view_someone_elses_application(client: Client) -> None:
    user = UserFactory()
    # pyre-ignore[28]: Investigate type stubs for factory-boy.
    other = UserFactory(email=f"other+{user.email}")

    qs = get_query_string(user)
    client.get(f"/login/magic{qs}")

    # pyre-ignore[28]: Investigate type stubs for factory-boy.
    application = ApplicationFactory(applicant=other)

    response = client.get(f"/apply/view/{application.id}")
    assert response.status_code == 404
