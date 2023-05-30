from sqlalchemy.orm import Session

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

def get_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Ticket).offset(skip).limit(limit).all()


def get_user_tickets(db: Session, skip: int= 0, limit: int = 100):
    return db.query(Ticket).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = Ticket(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

