
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base
from .group import Group

from sqlalchemy import Column, Integer, create_engine, text


from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase


class TicketType(Base):
    '''
    2. TicketType表
    '''
    __tablename__="ticket_type"

    id : Mapped[int] = Column(Integer,primary_key=True, autoincrement=True)
    name: Mapped[str] = '未命名工单'
    enabled: Mapped[bool] = True
    for_groups: Mapped[str]
    form_schema: Mapped[str]
    
