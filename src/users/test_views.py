from __future__ import annotations

from django.contrib.auth import get_user_model
from django.test import Client
import pytest

TEST_EMAIL = "user@example.org"

# pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
User = get_user_model()


@pytest.mark.django_db
# pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
def test_login_creates_new_user(client: Client) -> None:
    assert not User.objects.filter(email=TEST_EMAIL)
    client.post("/login", {"email": TEST_EMAIL})
    assert User.objects.filter(email=TEST_EMAIL)[0]


# pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
def test_login_requires_email(client: Client) -> None:
    response = client.post("/login")
    assert response.status_code not in (301, 302)
    assert b"this field is required" in response.content.lower()
