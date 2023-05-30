
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base
from .user import User
from .ticket import Ticket

from sqlalchemy import create_engine, text


from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase


class UserTicketAssoc(Base):
    '''
    3. User和Ticket关联表
    '''
    __tablename__="user_ticket_association"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    ticket_id: Mapped[int] = mapped_column(ForeignKey("ticket.id"), primary_key=True)

    context: Mapped[str]
    
    # association between Assocation -> Child
    user: Mapped["User"] = relationship(back_populates="user_associations")

    # association between Assocation -> Parent
    ticket: Mapped["Ticket"] = relationship(back_populates="ticket_associations")
