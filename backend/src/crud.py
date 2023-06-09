import json
from sqlalchemy.orm import Session
import schemas

from model.base import Base
from model.user import User
from model.ticket import Ticket
from model.group import Group
from model.ticket_type import TicketType

import schemas

def query_user_by_id(db: Session, user_id: int):
    t = db.query(User).filter(User.id==user_id).first()
    if not t:
        raise KeyError('No User With This Id Exist')
    else: 
        return t


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# 别改这个了。改好了。
def create_user(db: Session, user: schemas.UserCreate):
    from utils.hash import hash
    db_user = User(id=user.id, name=user.name,hashed_password=hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 改好了。别动它。
def get_tickets(db: Session, skip: int = 0, limit: int = 100)->schemas.TicketBrief:
    ts= db.query(Ticket).offset(skip).limit(limit).all()
    return [schemas.TicketBrief(id=t.id,title=t.title) for t in ts]


# 这个暂时搁置，暂时直接返回给用户所有工单，省点力气。
def get_user_tickets(db: Session, skip: int= 0, limit: int = 100):
    return db.query(Ticket).offset(skip).limit(limit).all()

# 写好了，不要动。
def get_ticket_detail(db: Session, id: int):
    import ticket_type.types as tttypes
    t = db.query(Ticket).filter(Ticket.id==id).first()
    if not t:
        raise KeyError('No Ticket With This Id Exist')
    ttm=tttypes.get_ticket_types_by_id(t.ticket_type_id)
    return schemas.TicketDetail(id=id,
                                ticket_type=tttypes.get_schema_by_id(id),
                                title=t.title,
                                form_model=t.form_model)

# 写好了。不要动。
def edit_ticket(db: Session, te:schemas.TicketEdit):
    t = db.query(Ticket).filter(Ticket.id==te.id).first()
    if not t:
        raise KeyError('No Ticket WIth This Id Exist')
    
    import ticket_type.types as tttypes
    ttm=tttypes.get_ticket_types_by_id(t.ticket_type_id)
    M=te.form_model
    (s,m) = ttm.postHandler(M.state, M)
    m.state=s
    
    t.form_model=m.json()
    db.commit()

# 写好了别动。
def create_ticket(db: Session, user_id:int, tc:schemas.TicketCreate):
    t = Ticket(
        title=tc.title,
        creater_user_id=user_id,
        ticket_type_id=tc.ticket_type_id)
    db.add(t)
    db.commit()
    db.refresh(t)
    import ticket_type.types as tttypes
    ttm = tttypes.get_schema_by_id(t.ticket_type_id)
    return schemas.TicketCreateSuccess(
        id=t.id,
        title=t.title,
        ticket_type_name=ttm.name,
        fields=ttm.fields,
        form_model=t.form_model
    )


# 写好了不要改。
def get_current_user_detail(db: Session, token:str)->schemas.UserDetail:
    from utils.token import parse_token
    obj = parse_token(token)
    id = obj['sub']
    u= db.query(User).filter(User.id==id).first()
    return schemas.UserDetail(id=id,name=u.name,groups=[g.name for g in u.groups])

def get_ticket_types()->list[schemas.TicketType]:
    import ticket_type.types as tttypes
    return [tttypes.get_schema_by_id(id) for id in tttypes.ticket_types]