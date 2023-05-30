
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base,user_group_assoc
from sqlalchemy import create_engine, text


from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase




class Group(Base):
    '''
    4. 用户组表. 一个用户组要绑定很多用户。
    '''
    __tablename__ = "user_group"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    # 一个用户组要绑定很多用户
    users: Mapped[list["User"]] = relationship(
        secondary=user_group_assoc,
        back_populates="groups"
    )

    def __repr__(self) -> str:
        return f"{self.name}"
