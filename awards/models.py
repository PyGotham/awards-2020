from datetime import datetime

from citext import CIText  # type: ignore[import]
from sqlalchemy import Column, Integer
from sqlalchemy.types import TIMESTAMP

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(CIText, nullable=False, unique=True)
    created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    modified = Column(
        TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
