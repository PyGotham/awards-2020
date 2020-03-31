from datetime import datetime
from typing import cast

from citext import CIText  # type: ignore[import]
from flask_security import RoleMixin, UserMixin  # type: ignore[import]
from flask_security.datastore import (  # type: ignore[import]
    SQLAlchemyDatastore,
    UserDatastore,
)
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.types import TIMESTAMP

from .db import Base


class Role(Base, RoleMixin):  # type: ignore
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(CIText, nullable=False, unique=True)
    description = Column(String(255), nullable=False, default="")
    created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    modified = Column(
        TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class User(Base, UserMixin):  # type: ignore
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


class SQLAlchemyUserDatastore(SQLAlchemyDatastore, UserDatastore):  # type: ignore
    def __init__(self, db: object) -> None:
        SQLAlchemyDatastore.__init__(self, db)
        UserDatastore.__init__(self, User, Role)

    def get_user(self, id: str) -> User:
        if _is_numeric(id):
            user = self.db.query(User).get(id)
        else:
            user = self.db.query(User).filter(User.email == id).first()
            if not user:
                user = User(email=id)
                self.db.add(user)
                self.db.commit()
        return cast(User, user)


def _is_numeric(value: str) -> bool:
    try:
        int(value)
    except ValueError:
        return False
    else:
        return True
