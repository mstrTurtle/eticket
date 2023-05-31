
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base
from .group import Group

from sqlalchemy import Column, Integer, create_engine, text,BOOLEAN


from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase


class TicketType(Base):
    '''
    2. TicketType表
    '''
    __tablename__="ticket_type"

    id : Mapped[int] = Column(Integer,primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String,default='未命名工单类型')
    enabled: Mapped[bool] = Column(BOOLEAN,default=True)
    for_group: Mapped[str]
    form_schema: Mapped[str]
    
