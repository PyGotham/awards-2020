from typing import Optional

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Session = sessionmaker()
session = scoped_session(Session)

Base = declarative_base()


def init_app(app: Flask) -> None:
    engine = create_engine(app.config["DATABASE_URI"])
    Session.configure(bind=engine)  # type: ignore[no-untyped-call]

    @app.teardown_request
    def remove_session(exception: Optional[Exception] = None) -> None:
        session.remove()  # type: ignore[no-untyped-call]
