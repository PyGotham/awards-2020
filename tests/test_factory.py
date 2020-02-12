from __future__ import annotations

from flask import Response
from flask.testing import FlaskClient


def test_home(client: FlaskClient[Response]) -> None:
    response = client.get("/")

    assert b"I'd like a ticket" in response.data
    assert b"I'd like travel reimbursement, lodging, and/or a ticket" in response.data
