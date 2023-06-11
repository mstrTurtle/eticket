
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base
from .workflow import Workflow

from sqlalchemy import Column, Integer, create_engine, text


from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase


class Ticket(Base):
    '''
    3. User和Ticket关联表
    '''
    __tablename__="ticket"

    id: Mapped[int] = Column(Integer,primary_key=True, autoincrement=True)
    title: Mapped[str]

    # meta
    creator_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    edit_time: Mapped[int]
    create_time: Mapped[int]

    models: Mapped[str] = Column(String,default='{}')
    workflow_id: Mapped[int] = mapped_column(ForeignKey("workflow.id"))
    
    workflow: Mapped["Workflow"] = relationship(primaryjoin='Ticket.workflow_id==Workflow.id')
    creator: Mapped["User"] = relationship(primaryjoin='Ticket.creator_id==User.id')

    state: Mapped[str]

    # 这东西是否应当删去
    @property
    def creator_name(self):
        return self.creator.name
    
    @property
    def workflow_name(self):
        return self.workflow.name
    
    @property
    def models_obj(self):
        import json
        return json.loads(self.models)
    
    @models_obj.setter
    def models_obj(self, value):
        # print("Setting name to " + value)
        import json
        self.models = json.dumps(value)
    
    @property
    def valid_flow(self)->list[str]:
        flows_obj = self.workflow.flows_obj
        return [flow[2] for flow in flows_obj if flow[0] == self.state ]
    
    @property
    def meta(self):
        return {
            "creator_id": self.creator_id,
            "creator_name": self.creator.name,
            "edit_time": self.edit_time,
            "create_time": self.create_time            
        }