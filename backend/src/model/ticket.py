
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base
from .group import Group
from .user_ticket_assoc import UserTicketAssoc

from sqlalchemy import create_engine, text


from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase


class Ticket(Base):
    '''
    2. Ticket表
    '''
    __tablename__="ticket"

    id : Mapped[int]
    name: Mapped[str]
    statemachine_definition: Mapped[str]
    

    users: Mapped[list["Group"]] = relationship(
        secondary="user_ticket_association",back_populates="tickets", viewonly=True
    )

    # association between Parent -> Association -> Child
    user_associations: Mapped[List["UserTicketAssoc"]] = relationship(
        back_populates="ticket"
    )

