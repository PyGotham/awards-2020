from __future__ import annotations

import os.path

from _pytest.fixtures import FixtureRequest  # type: ignore[import]
from alembic.command import downgrade, upgrade  # type: ignore[import]
from alembic.config import Config  # type: ignore[import]
from flask import Flask, Response
from flask.testing import FlaskClient
import pytest  # type: ignore[import]
from sqlalchemy import event
from sqlalchemy.orm import Session
from sqlalchemy.orm.session import SessionTransaction

from awards.db import session
from awards.main import create_app


@pytest.fixture(scope="session")  # type: ignore[misc]
def app() -> Flask:
    return create_app(test_config={"TESTING": True})


@pytest.fixture  # type: ignore[misc]
def client(app: Flask) -> FlaskClient[Response]:
    return app.test_client()


@pytest.fixture(scope="session", autouse=True)  # type: ignore[misc]
def create_database_tables(request: FixtureRequest, app: Flask) -> None:
    config = Config(os.path.abspath("alembic.ini"))
    upgrade(config=config, revision="head")

    @event.listens_for(  # type: ignore[no-untyped-call,misc]
        Session, "after_transaction_end"
    )
    def reset_savepoint(session: Session, transaction: SessionTransaction) -> None:
        if transaction.nested and not transaction.parent.nested:
            session.begin_nested()

    def remove_database_tables() -> None:
        downgrade(config=config, revision="base")

    request.addfinalizer(remove_database_tables)


@pytest.fixture(autouse=True)  # type: ignore[misc]
def transaction(request: FixtureRequest) -> None:
    request.addfinalizer(session.remove)

    session.begin_nested()
