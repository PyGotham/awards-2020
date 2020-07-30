from django.contrib.auth import get_user_model
from django.db import IntegrityError
import pytest

TEST_EMAIL = "user@example.org"

pytestmark = pytest.mark.django_db

User = get_user_model()


def test_cannot_create_without_email() -> None:
    with pytest.raises(IntegrityError):  # type: ignore
        User.objects.create(email=None)


def test_email_is_case_insensitive() -> None:
    user1, _ = User.objects.get_or_create(email=TEST_EMAIL.lower())
    user2, _ = User.objects.get_or_create(email=TEST_EMAIL.upper())
    assert user1 == user2


@pytest.mark.parametrize("number_of_characters", range(10))
def test_email_is_redacted(number_of_characters: int) -> None:
    user = User(email=f"a{'b' * number_of_characters}@example.org")
    assert str(user) == f"a{'*' * number_of_characters}@example.org"
