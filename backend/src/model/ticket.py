
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

import json


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

    history: Mapped[str] = mapped_column(String,default="[]")

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
    
    @property
    def history_obj(self):
        return json.loads(self.history)
    
    @history_obj.setter
    def history_obj(self, val):
        self.history = json.dumps(val)

    @property
    def overdue(self):
        from utils.time import is_current_week, is_today, unix_to_datetime, seconds_ago
        overdue_seconds_limit = 3600 * 12 # 相当于12小时
        return not self.done and seconds_ago(unix_to_datetime(self.create_time)) > overdue_seconds_limit
    
    @property
    def done(self):
        return (len(self.valid_flow) == 0)