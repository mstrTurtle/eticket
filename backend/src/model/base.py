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

from logger import logger


# database URL格式：
# dialect+driver://username:password@host:port/database
import os
memory_mode=os.getenv('ETICKET_MEMORY_MODE')
db_passwd=os.getenv('ETICKET_DB_PASSWD')

logger.info(f"base module initialzing, memory_mode={bool(memory_mode)}, db_passwd={bool(db_passwd)}.")

if memory_mode:
    SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///:memory:"
    from sqlalchemy.pool import StaticPool
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
elif db_passwd:
    SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:{db_passwd}@localhost/eticket"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
    )
else:
    raise SystemExit('你既没有指定ETICKET_MEMORY_MODE又没有提供ETICKET_DB_PASSWD环境变量')


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass

from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

# user_group_assoc = Table(
#     "user_group_association",
#     Base.metadata,
#     Column("user_id", ForeignKey("user.id")),
#     Column("user_group_id", ForeignKey("user_group.id")),
# )

class UserGroupAssoc(Base):
    __tablename__ = "user_group_assoc"
    user_id = Column("user_id", ForeignKey("user.id"), primary_key=True)
    user_group_id = Column("user_group_id", ForeignKey("user_group.id"), primary_key=True)
