# from enum import Enum
from sqlalchemy import create_engine, text, Column, Table


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


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:zr20020515@localhost/eticket"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass

from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

user_group_assoc = Table(
    "user_group_association",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("user_group_id", ForeignKey("user_group.id")),
)