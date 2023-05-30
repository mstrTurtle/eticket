from sqlalchemy.orm import Session
import backend.src.schemas

from model.base import Base
from model.user import User
from model.ticket import Ticket
from model.group import Group
from model.ticket_type import TicketType

import schemas


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
    return [schemas.TicketBrief(id=t.id,title=t.titile) for t in ts]


# 这个暂时搁置，暂时直接返回给用户所有工单，省点力气。
def get_user_tickets(db: Session, skip: int= 0, limit: int = 100):
    return db.query(Ticket).offset(skip).limit(limit).all()

# 写好了，不要动。
def get_ticket_detail(db: Session, id: int):
    t = db.query(Ticket).filter(Ticket.id==id).first()
    return schemas.TicketDetail(id=id,
                                ticket_type_name=t.ticket_type.name,
                                title=t.title,
                                form_model=t.form_model,
                                form_schema=t.ticket_type.form_schema)

# 写好了。不要动。
def edit_ticket(db: Session, id: int, model: str):
    t = db.query(Ticket).filter(Ticket.id==id).first()
    t.form_model=model
    db.commit()

# 写好了别动。
def create_ticket(db: Session, user_id:int, tc:schemas.TicketCreate):
    t = Ticket(
        title=tc.title,
        create_user_id=user_id,
        ticket_type_id=tc.ticket_type_id)
    db.add(t)
    db.commit()

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = Ticket(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# 写好了不要改。
def get_current_user_detail(db: Session, token:str)->schemas.UserDetail:
    from utils.token import parse_token
    obj = parse_token(token)
    id = obj['sub']
    u= db.query(User).filter(User.id==id).first()
    return schemas.UserDetail(id=id,name=u.name,groups=[g.name for g in u.groups])