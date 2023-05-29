from enum import Enum
from sqlalchemy import create_engine, text


def __createMemoryEngine():
    engine = create_engine("sqlite+pysqlite:///:memory:", future=True, echo=True)
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())
    
    return engine

def __createAll(Base, engine):
    Base.metadata.create_all(engine)

engine = None

def createEngineWithCreateAll(Base):
    global engine
    if not engine:
        engine=__createMemoryEngine()
        __createAll(Base = Base,engine = engine)
    return engine

from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class User(Base):
    '''
    1. User表.
    '''
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    hashed_password: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))

    groups: Mapped[list["Group"]] = relationship(
        back_populates="users"
    )

    tickets: Mapped[list["Group"]] = relationship(
        secondary="user_ticket_association",back_populates="users", viewonly=True
    )

    # association between Parent -> Association -> Child
    ticket_associations: Mapped[List["UserTicketAssoc"]] = relationship(
        back_populates="user"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


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


class Group(Base):
    '''
    4. 用户组表. 一个用户组要绑定很多用户。
    '''
    __tablename__ = "user_group"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    # 一个用户组要绑定很多用户
    users: Mapped[list["User"]] = relationship(
        back_populates="groups"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}"
