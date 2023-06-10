from pydantic import BaseModel

class Workflow(BaseModel):
    id: int
    name: str
    groups: list[str]
    fields: dict[str,list[dict]]

class TicketBase(BaseModel):
    pass

class TicketBrief(TicketBase):
    id: int
    title: str

class TDTicket(BaseModel):
    id: int
    title: str
    creator_id: int
    creator_name: str
    edit_time: int
    create_time: int
    state: str
    models: dict

class TDWorkflow(BaseModel):
    name: str
    valid_flow: list[str]

class TicketDetail(TicketBase):
    ticket: TDTicket
    workflow: TDWorkflow

class TicketCreate(TicketBase):
    workflow_id: int
    title: str

class TicketCreateSuccess(TicketBase):
    id: int
    title: str
    workflow_name: str
    fields: dict[str,list[dict]]
    form_model: str

    class Config:
        orm_mode = True

class FormModel(BaseModel):
    state: str
    models : list[dict]

class TicketEdit(TicketBase):
    id: int
    form_model: FormModel


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