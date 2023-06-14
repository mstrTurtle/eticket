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
        "name":"王临川",
        "password":"passwd"
    },
    {
        "id":1,
        "name":"王右军",
        "password":"passwd"
    },
    {
        "id":2,
        "name":"李太白",
        "password":"passwd"
    },
    {
        "id":3,
        "name":"陆子静",
        "password":"passwd"
    },
    {
        "id":4,
        "name":"朱元晦",
        "password":"passwd",
    },    
]

for user in users:
    from utils.hash import hash
    user['hashed_password'] = hash(user['password'])

statesA = '''
[
    {
      "name": "发起维修",
      "groups": ["后勤"],
      "fields": [
                    {
                        "type": "str",
                        "name": "事由",
                        "required": true
                    }
                ]
    },
    {
      "name": "审批维修1",
      "groups": ["领导"],
      "fields": [
                    {
                        "id": 1,
                        "type": "str",
                        "name": "审批意见",
                        "required": true
                    }
                ]
    },
    {
      "name": "执行运维",
      "groups": ["运维"],
      "fields": [
                    {
                        "id": 1,
                        "type": "check",
                        "name": "完成与否",
                        "required": true
                    },
                    {
                        "id": 2,
                        "type": "radio",
                        "selections": [
                        "一棵树",
                        "两棵树"
                        ],
                        "name": "浇了多少水",
                        "required": true
                    },
                    {
                        "id": 3,
                        "type": "str",
                        "name": "完成情况简述",
                        "required": false
                    }
                ]
    }
  ]
'''

statesB='''
[
    {
      "name": "发起采购",
      "groups": ["后勤"],
      "fields": [
                    {
                        "type": "str",
                        "name": "事由",
                        "required": true
                    }
                ]
    },
    {
      "name": "审批采购1",
      "groups": ["领导"],
      "fields": [
                    {
                        "id": 1,
                        "type": "str",
                        "name": "审批意见",
                        "required": true
                    }
                ]
    },
    {
      "name": "执行采购",
      "groups": ["采购"],
      "fields": [
                    {
                        "id": 1,
                        "type": "check",
                        "name": "完成与否",
                        "required": true
                    },
                    {
                        "id": 2,
                        "type": "radio",
                        "selections": [
                        "一棵树",
                        "两棵树"
                        ],
                        "name": "买了多少棵树",
                        "required": true
                    },
                    {
                        "id": 3,
                        "type": "str",
                        "name": "完成情况简述",
                        "required": false
                    }
                ]
    }
  ]
'''

flowsA = '''
[
    ["发起维修", "审批维修1", "维修送审"],
    ["审批维修1", "执行运维", "审批通过"],
    ["审批维修1", "发起维修", "驳回请求"],
    ["执行运维", "关闭", "完成工单"]
  ]
'''

flowsB = '''
[
    ["发起采购", "审批采购1", "采购送审"],
    ["审批采购1", "执行采购", "审批通过"],
    ["审批采购1", "发起采购", "驳回请求"],
    ["执行采购", "关闭", "完成工单"]
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

modelsA = '''
{
    "A":{
        "事由": "花要死了"
    },
    "B":{

    },
    "C":{
        "完成与否": false,
        "浇了多少水": "一棵树",
        "完成情况简述":"不行不行"
    }
}
'''

modelsB = '''
{
    "A":{
        "事由": "草不够了"
    },
    "B":{

    },
    "C":{
        "完成与否": true,
        "买了多少棵树": "一棵树",
        "完成情况简述":"可以的"
    }
}
'''

tickets=[
    {
        "id":0,
        "workflow_id": 0,
        "title": "维修花草树木工单",
        "creator_id": 1,
        "edit_time": 1686446917,
        "create_time": 1686446900,
        "state": "发起维修",
        "models": modelsA,
    },
    {
        "id":1,
        "workflow_id": 1,
        "title": "采购草皮工单",
        "creator_id": 2,
        "edit_time": 1686446917,
        "create_time": 1686446900,
        "state": "审批采购1",
        "models": modelsB,
    },
    {
        "id":2,
        "workflow_id": 0,
        "title": "园艺浇水工单",
        "creator_id": 3,
        "edit_time": 1686446917,
        "create_time": 1686446900,
        "state": "执行运维",
        "models": modelsA,
    },
    {
        "id":3,
        "workflow_id": 1,
        "title": "草皮采买工单",
        "creator_id": 4,
        "edit_time": 1686446917,
        "create_time": 1686446900,
        "state": "执行采购",
        "models": modelsB,
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