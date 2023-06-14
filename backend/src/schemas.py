from pydantic import BaseModel

class Workflow(BaseModel):
    id: int
    name: str
    enabled: bool
    # groups: list[str]
    states_obj: list
    flows_obj: list

    class Config:
        orm_mode = True

class TicketBase(BaseModel):
    pass

class TicketMeta(BaseModel):
    creator_id: int
    creator_name: str
    edit_time: int
    create_time: int

    class Config:
        orm_mode = True

class TicketBrief(TicketBase):
    id: int
    title: str
    meta: TicketMeta
    state: str
    workflow_name: str
    overdue: bool
    done: bool

    class Config:
        orm_mode = True

class TDTicket(BaseModel):
    id: int
    title: str
    meta: TicketMeta
    state: str
    # models_obj: dict
    valid_flow: list[str]
    history_obj: list

    class Config:
        orm_mode = True

class TDWorkflow(BaseModel):
    id: int
    name: str
    states_obj: list
    flows_obj: list

    class Config:
        orm_mode = True

class FormReprValue(BaseModel):
    name: str
    active: bool
    model: dict
    fields: list

class TicketDetail(TicketBase):
    ticket: TDTicket
    # workflow: TDWorkflow
    state_names: list[str]
    form_repr: dict[str,FormReprValue]

class TicketCreate(TicketBase):
    workflow_id: int
    title: str

class TicketCreateSuccess(TicketBase):
    id: int
    class Config:
        orm_mode = True

class TicketEdit(TicketBase):
    id: int
    flow_name: str
    model: dict


class UserBase(BaseModel):
    id: int


class UserCreate(UserBase):
    name:str
    password: str


class UserDetail(UserBase):
    id: int
    name: str
    groups: list[str]

    class Config:
        orm_mode = True

class Statics(BaseModel):
    day_done: int
    day_total:int
    week_done: int
    week_total: int
    overdue_cnt: int
    overdues: list
    total: int