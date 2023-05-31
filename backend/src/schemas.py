from pydantic import BaseModel

class TicketBase(BaseModel):
    pass

class TicketBrief(TicketBase):
    id: int
    title: str

class TicketDetail(TicketBase):
    id: int
    ticket_type_name: str
    title: str
    form_schema: str
    form_model: str

class TicketCreate(TicketBase):
    ticket_type_id: int
    title: str

class TicketCreateSuccess(TicketBase):
    id: int
    title: str
    ticket_type_name: str
    form_schema: str
    form_model: str

    class Config:
        orm_mode = True

class TicketEdit(TicketBase):
    id: int
    form_model: str

class TicketType(BaseModel):
    id: int
    name: str
    enabled: bool
    for_group: str
    form_schema: str

class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


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