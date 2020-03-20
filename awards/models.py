from datetime import datetime

from citext import CIText  # type: ignore[import]
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.types import TIMESTAMP

from .db import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(CIText, nullable=False, unique=True)
    description = Column(String(255), nullable=False, default="")
    created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    modified = Column(
        TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(CIText, nullable=False, unique=True)
    created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    modified = Column(
        TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    roles = relationship(
        "Role",
        secondary="user_roles",
        backref=backref("users", lazy="dynamic"),  # type: ignore[no-untyped-call]
    )


class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))

    __table_args__ = (UniqueConstraint("user_id", "role_id"),)
