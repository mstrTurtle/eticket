
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base
from .ticket_type import TicketType

from sqlalchemy import Column, Integer, create_engine, text


from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase


class Ticket(Base):
    '''
    3. User和Ticket关联表
    '''
    __tablename__="ticket"

    id: Mapped[int] = Column(Integer,primary_key=True, autoincrement=True)
    title: Mapped[str]
    ticket_type_id: Mapped[int] = mapped_column(ForeignKey("ticket_type.id"))
    creater_user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    
    form_model: Mapped[str] = "{}"
    
    ticket_type: Mapped["TicketType"] = relationship()