from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session
from .base import Base,SessionLocal,engine,UserGroupAssoc
from .user import User
from .ticket import Ticket
from .group import Group
from .workflow import Workflow

users=[
    {
        "id":0,
        "name":"turtle",
        "password":"passwd"
    },
    {
        "id":1,
        "name":"aa",
        "password":"passwd"
    },
    {
        "id":2,
        "name":"xx",
        "password":"passwd"
    },
    {
        "id":3,
        "name":"yy",
        "password":"passwd"
    },
    {
        "id":4,
        "name":"zz",
        "password":"passwd",
    },    
]

for user in users:
    from utils.hash import hash
    user['hashed_password'] = hash(user['password'])

statesA = '''
[
    {
      "name": "A",
      "groups": ["后勤"],
      "fields": [
                    {
                        "type": "str",
                        "name": "事由",
                        "required": true,
                        "value": "花要死了"
                    }
                ]
    },
    {
      "name": "B",
      "groups": ["领导"],
      "fields": [
                    {
                        "id": 1,
                        "type": "str",
                        "name": "审批意见",
                        "required": true,
                        "value": "重新写"
                    }
                ]
    },
    {
      "name": "C",
      "groups": ["运维"],
      "fields": [
                    {
                        "id": 1,
                        "type": "check",
                        "name": "完成与否",
                        "required": true,
                        "value": false
                    },
                    {
                        "id": 2,
                        "type": "radio",
                        "selections": [
                        "一棵树",
                        "两棵树"
                        ],
                        "name": "浇了多少水",
                        "required": true,
                        "value": "一棵树"
                    },
                    {
                        "id": 3,
                        "type": "str",
                        "name": "完成情况简述",
                        "required": false,
                        "value": "大中午根本浇不了水，一浇水等着烧苗吧。"
                    }
                ]
    }
  ]
'''

statesB='''
[
    {
      "name": "A",
      "groups": ["后勤"],
      "fields": [
                    {
                        "type": "str",
                        "name": "事由",
                        "required": true,
                        "value": "花要死了"
                    }
                ]
    },
    {
      "name": "B",
      "groups": ["领导"],
      "fields": [
                    {
                        "id": 1,
                        "type": "str",
                        "name": "审批意见",
                        "required": true,
                        "value": "重新写"
                    }
                ]
    },
    {
      "name": "C",
      "groups": ["采购"],
      "fields": [
                    {
                        "id": 1,
                        "type": "check",
                        "name": "完成与否",
                        "required": true,
                        "value": false
                    },
                    {
                        "id": 2,
                        "type": "radio",
                        "selections": [
                        "一棵树",
                        "两棵树"
                        ],
                        "name": "买了多少颗树",
                        "required": true,
                        "value": "一棵树"
                    },
                    {
                        "id": 3,
                        "type": "str",
                        "name": "完成情况简述",
                        "required": false,
                        "value": "树要阔叶落叶的比较符合这里气候，所以我买了这个"
                    }
                ]
    }
  ]
'''

flowsA = '''
[
    ["A", "B", "维修送审"],
    ["B", "C", "审批通过"],
    ["B", "A", "驳回请求"],
    ["C", "*", "完成工单"]
  ]
'''

flowsB = '''
[
    ["A", "B", "采购送审"],
    ["B", "C", "审批通过"],
    ["B", "A", "驳回请求"],
    ["C", "*", "完成工单"]
  ]
'''

workflows=[
    {
        "id": 0,
        "name": "运维工单",
        "states":statesA,
        "flows":flowsA
    },
    {
        "id": 1,
        "name": "采购工单",
        "states":statesB,
        "flows":flowsB
    }
]

tickets=[
    {
        "id":0,
        "title": "MyTicketOne",
        "creator_id": 1,
        "edit_time": 1686446917,
        "create_time": 1686446900,
        "workflow_id": 0,
        "state": "A",
    },
    {
        "id":1,
        "workflow_id": 1,
        "title": "MyTicketTwo",
        "creator_id": 1,
        "edit_time": 1686446917,
        "create_time": 1686446900,
        "workflow_id": 0,
        "state": "A",
    },
    {
        "id":2,
        "workflow_id": 0,
        "title": "MyTicketThree",
        "creator_id": 1,
        "edit_time": 1686446917,
        "create_time": 1686446900,
        "workflow_id": 0,
        "state": "A",
    },
    {
        "id":3,
        "workflow_id": 1,
        "title": "MyTicketFour",
        "creator_id": 1,
        "edit_time": 1686446917,
        "create_time": 1686446900,
        "workflow_id": 0,
        "state": "A",
    }

]

groups=[
    {
        "id":0,
        "name":"后勤"
    },
    {
        "id":1,
        "name":"领导"
    },
    {
        "id":2,
        "name":"运维"
    },

]

user_group_assocs=[
    {
        "user_id":0,
        "user_group_id":0
    },
    {
        "user_id":0,
        "user_group_id":1
    },
    {
        "user_id":0,
        "user_group_id":2
    },
    {
        "user_id":1,
        "user_group_id":0
    },
    {
        "user_id":1,
        "user_group_id":1
    },
    {
        "user_id":2,
        "user_group_id":1
    },
    {
        "user_id":3,
        "user_group_id":2
    },
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
    from logger import logger


    Base.metadata.drop_all(engine)
    logger.info("db population dropped all")

    Base.metadata.create_all(engine)
    logger.info("db population created all")


    with SessionLocal() as session:
        
        logger.info("db population session begin")
        # for user in users:
        #     u=User(**user)
        #     session.add(u)
        session.execute(
            insert(User),
            users
        )
        session.execute(
            insert(Workflow),
            workflows
        )        
        session.execute(
            insert(Ticket),
            tickets
        )
        session.execute(
            insert(Group),
            groups
        )
        session.execute(
            insert(UserGroupAssoc),
            user_group_assocs
        )
        session.commit()
        logger.info("db population commited")
        
if __name__=="__main__":
    populate()