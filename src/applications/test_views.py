from __future__ import annotations

from django.contrib.auth import get_user_model
from django.http import Http404, HttpRequest
from django.test import Client
from factory.django import DjangoModelFactory
import pytest
from sesame.utils import get_query_string

from applications.models import Application
from applications.views import apply


# pyre-ignore[13]: Investigate type stubs for factory-boy.
class ApplicationFactory(DjangoModelFactory):
    class Meta:
        model = Application

    id: int
    background = "BACKGROUND"
    reason_to_attend = "REASON"
    type = Application.Type.SCHOLARSHIP


class UserFactory(DjangoModelFactory):
    class Meta:
        # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
        model = get_user_model()
        django_get_or_create = ("email",)

    email = "user@example.org"


@pytest.mark.django_db
# pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
def test_that_one_of_form_type_and_pk_is_required_by_apply(client: Client) -> None:
    user = UserFactory()
    qs = get_query_string(user)
    client.get(f"/login/magic{qs}")

    request = HttpRequest()
    request.user = user
    # pyre-ignore[16]: pyre doesn't think ExceptionInfo as an __enter__.
    with pytest.raises(Http404):
        apply(request, form_type=None, pk=None)


@pytest.mark.django_db
# pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
def test_user_can_edit_their_application(client: Client) -> None:
    user = UserFactory()
    qs = get_query_string(user)
    client.get(f"/login/magic{qs}")

    # pyre-ignore[28]: Investigate type stubs for factory-boy.
    application = ApplicationFactory(applicant=user)

    expected = f"{application.background} changed"

    response = client.post(
        f"/apply/edit/{application.id}",
        {"background": expected, "reason_to_attend": application.reason_to_attend},
    )
    assert response.status_code == 200

    modified_application = Application.objects.get(pk=application.id)
    assert modified_application.background == expected


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
