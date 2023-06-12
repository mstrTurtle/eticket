import json
from sqlalchemy.orm import Session
import schemas

from model.base import Base
from model.user import User
from model.ticket import Ticket
from model.group import Group
from model.workflow import Workflow

from utils.time import get_timestamp_now

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

# def make_ticket_brief(t:Ticket)->schemas.TicketBrief:
#     # t.asdict()
#     meta =  schemas.TicketMeta.from_orm(t)
#     t.meta = meta
#     tb = schemas.TicketBrief.from_orm(t)
#     return tb

# def make_ticket_detail(t:Ticket):
#     ...

# 改好了。别动它。
def get_tickets(db: Session, skip: int = 0, limit: int = 100)->schemas.TicketBrief:
    ts= db.query(Ticket).offset(skip).limit(limit).all()
    return [t for t in ts]


# 这个暂时搁置，暂时直接返回给用户所有工单，省点力气。
def get_user_tickets(db: Session, skip: int= 0, limit: int = 100):
    return db.query(Ticket).offset(skip).limit(limit).all()

# 写好了，不要动。
def get_ticket_detail(db: Session, id: int):
    import ticket_type.types as tttypes
    t = db.query(Ticket).filter(Ticket.id==id).first()
    if not t:
        raise KeyError('No Ticket With This Id Exist')
    w = t.workflow
    # meta = schemas.TicketMeta.from_orm(t)
    # t.meta = meta
    # ttm=tttypes.get_ticket_types_by_id(t.workflow_id)
    return schemas.TicketDetail(ticket=schemas.TDTicket.from_orm(t),
                                workflow=schemas.TDWorkflow.from_orm(w))

def test_flow_name_valid(t:Ticket,w:Workflow,state:str,flow_name:str)->bool:
    # flow_name_valid = False
    # for flow in w.flows_obj:
    #     cur_from = flow[0]
    #     cur_flow_name = flow[2]
    #     if cur_from != state:
    #         continue
    #     if cur_flow_name == flow_name:
    #         flow_name_valid = True
    #         break
    flow_name_valid = (flow_name in t.valid_flow)
    if not flow_name_valid:
        raise KeyError(f'Flow Name Not Valid, Fr = {state}, ValidNames = {t.valid_flow}')


def get_flow_name_to(w:Workflow,flow_name:str)->str:
    for flow in w.flows_obj:
        cur_from = flow[0]
        cur_to = flow[1]
        cur_flow_name = flow[2]
        if cur_flow_name == flow_name:
            return cur_to
    raise KeyError('Flow Name Not Found')
    
def update_ticket_model(t:Ticket, fr:str, model:dict):
    '''具有side effect，只把它当做是个过程。
    类似宏展开的东西，并没有做什么抽象'''
    obj_copy = t.models_obj
    obj_copy[fr] = model
    t.models_obj = obj_copy

# 写好了。不要动。
def edit_ticket(db: Session, te:schemas.TicketEdit):
    t = db.query(Ticket).filter(Ticket.id==te.id).first()
    state_fr = t.state
    if not t:
        raise KeyError('No Ticket WIth This Id Exist')
    w = t.workflow
    flow_name_valid = test_flow_name_valid(t,w,t.state,te.flow_name)
    to = get_flow_name_to(w,te.flow_name)
    t.state = to
    update_ticket_model(t,state_fr,te.model)
    db.add(t)
    db.commit()
    db.refresh(t)

    # import ticket_type.types as tttypes
    # ttm=tttypes.get_ticket_types_by_id(t.ticket_type_id)
    # M=te.form_model
    # (s,m) = ttm.postHandler(M.state, M)
    # m.state=s
    
    # t.form_model=m.json()
    # db.commit()

# 写好了别动。
def create_ticket(db: Session, user_id:int, tc:schemas.TicketCreate):
    
    w = db.query(Workflow).filter(Workflow.id==tc.workflow_id).first()
    if w is None:
        raise KeyError('Wrong Workflow Key')
    t = Ticket(
        title=tc.title,
        creator_id=user_id,
        edit_time = get_timestamp_now(),
        create_time = get_timestamp_now(),
        models='{}',
        workflow_id=tc.workflow_id,
        state=w.first_state)
    db.add(t)
    db.commit()
    db.refresh(t)
    # import ticket_type.types as tttypes
    # ttm = tttypes.get_schema_by_id(t.ticket_type_id)
    return schemas.TicketCreateSuccess(
        id=t.id,
        title=t.title,
        workflow_name=w.name,
        fields=w.states,
        form_model=t.models
    )


# 写好了不要改。
def get_current_user_detail(db: Session, token:str)->schemas.UserDetail:
    from utils.token import parse_token
    obj = parse_token(token)
    id = obj['sub']
    u= db.query(User).filter(User.id==id).first()
    return schemas.UserDetail(id=id,name=u.name,groups=[g.name for g in u.groups])

def get_workflows(db: Session)->list[schemas.Workflow]:
    # import ticket_type.types as tttypes
    # return [tttypes.get_schema_by_id(id) for id in tttypes.ticket_types]
    ws = db.query(Workflow).all()
    return [schemas.Workflow.from_orm(w) for w in ws]