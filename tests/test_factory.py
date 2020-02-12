from __future__ import annotations

from flask import Response
from flask.testing import FlaskClient


def test_hello(client: FlaskClient[Response]) -> None:
    response = client.get("/hello")
    assert response.data == b"hello, world"
