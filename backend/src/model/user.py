
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base,user_group_assoc
from .group import Group
from .ticket import Ticket
from .user_ticket_assoc import UserTicketAssoc

from sqlalchemy import create_engine, text


from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase



class User(Base):
    '''
    1. User表.
    '''
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    hashed_password: Mapped[str] = mapped_column(String(30))
    email: Mapped[str|None] = mapped_column(String(30))

    groups: Mapped[list["Group"]] = relationship(
        secondary=user_group_assoc,
        back_populates="users"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

