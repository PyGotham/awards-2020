from flask_security.datastore import UserDatastore  # type: ignore[import]
import pytest  # type: ignore[import]

from awards.db import session
from awards.models import SQLAlchemyUserDatastore, _is_numeric


@pytest.fixture  # type: ignore
def datastore() -> UserDatastore:
    return SQLAlchemyUserDatastore(session)


def test_datastore_get_user(datastore: UserDatastore) -> None:
    datastore.create_user(email="awards@pygotham.org")
    session.commit()  # type: ignore[no-untyped-call]

    assert datastore.get_user("awards@pygotham.org")


def test_datastore_get_user_not_found(datastore: UserDatastore) -> None:
    assert datastore.get_user("awards@pygotham.org") is None


@pytest.mark.parametrize("value", ("0", "-1", "1", "10"))  # type: ignore
def test_is_numeric(value: str) -> None:
    assert _is_numeric(value)


@pytest.mark.parametrize("value", ("", "a", "1.0"))  # type: ignore
def test_is_not_numeric(value: str) -> None:
    assert not _is_numeric(value)
