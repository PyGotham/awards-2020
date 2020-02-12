from __future__ import annotations

from flask import Flask, Response
from flask.testing import FlaskClient
import pytest  # type: ignore[import]

from rewards.main import create_app


@pytest.fixture  # type: ignore[misc]
def app() -> Flask:
    return create_app(test_config={"TESTING": True})


@pytest.fixture  # type: ignore[misc]
def client(app: Flask) -> FlaskClient[Response]:
    return app.test_client()
