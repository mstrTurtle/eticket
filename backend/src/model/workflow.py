
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base
from .group import Group

from sqlalchemy import Column, Integer, create_engine, text,BOOLEAN


from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase


class Workflow(Base):
    '''
    2. Workflow表
    '''
    __tablename__="workflow"

    id : Mapped[int] = Column(Integer,primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String,default='未命名工单类型')
    enabled: Mapped[bool] = Column(BOOLEAN,default=True)
    states: Mapped[str]
    flows: Mapped[str]

    @property
    def first_state(self)->str:
        import json
        obj = json.loads(self.states)
        return obj[0]['name']
    
    @property
    def flows_obj(self):
        import json
        print()
        o = json.loads(self.flows)
        # raise Exception(f'type o is {type(o)}')
        return o
    
    @property
    def states_obj(self):
        import json
        return json.loads(self.states)
    
    @property
    def state_names(self)->list[str]:
        ss = self.states_obj
        return [s['name'] for s in ss]