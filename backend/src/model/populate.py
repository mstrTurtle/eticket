from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session
from .base import Base,SessionLocal,engine
from .user import User
from .ticket import Ticket
from .group import Group
from .ticket_type import TicketType

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


from sqlalchemy.schema import DropTable
from sqlalchemy.ext.compiler import compiles

@compiles(DropTable, "postgresql")
def _compile_drop_table(element, compiler, **kwargs):
    '''
        专门给PGSQL用的强制删除关系表的东西。否则drop_all删不掉表。
        https://stackoverflow.com/questions/38678336/sqlalchemy-how-to-implement-drop-table-cascade
        You can customize the compilation of constructs like this.
        This appends CASCADE to the DROP TABLE statement issued for the postgresql dialect while keeping all other dialects the same.
    '''
    return compiler.visit_drop_table(element) + " CASCADE"


def populate():
    # database URL格式：
    # dialect+driver://username:password@host:port/database

    # url="postgresql+psycopg2://postgres:zr20020515@localhost/eticket"
    # engine = create_engine(url, echo=True)
    # Base.metadata.create_all(engine)

    Base.metadata.drop_all(engine)
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