from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session
from .base import Base,SessionLocal,engine
from .user import User
from .ticket import Ticket
from .group import Group
from .user_ticket_assoc import UserTicketAssoc

users=[
    {
        "id":101,
        "name":"turtle",
        "hashed_password":"passwd"
    },
    {
        "id":202,
        "name":"xx",
        "hashed_password":"passwd"
    },
    {
        "id":303,
        "name":"yy",
        "hashed_password":"passwd"
    },
    {
        "id":404,
        "name":"zz",
        "hashed_password":"passwd"
    },    
]

tickets=[
    {"id":400,
    "name":"zz",}

]

def populate():
    # database URL格式：
    # dialect+driver://username:password@host:port/database

    # url="postgresql+psycopg2://postgres:zr20020515@localhost/eticket"
    # engine = create_engine(url, echo=True)
    # Base.metadata.create_all(engine)

    Base.metadata.create_all(engine)


    with SessionLocal() as session:
        input('按回车确认增加user')
        # for user in users:
        #     u=User(**user)
        #     session.add(u)
        session.execute(
            insert(User),
            users
        )
        session.commit()
        
populate()