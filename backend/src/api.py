from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Required

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated, Optional

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model.base import Base,engine,SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

app = FastAPI()

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        await db
    finally:
        db.close()

# 设置CORS中间件
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()

class User(BaseModel):
    id: str
    password: str

class LoginInfo(BaseModel):
    token:str
    id:str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

users_db = {
    "turtle": {
        "role": "后勤",
        "age": 24,
        "password": "passwd"
    },
    "xx": {
        "role": "后勤",
        "age": 24,
        "password": "passwd"
    },
    "yy": {
        "role": "领导",
        "age": 24,
        "password": "passwd"
    },
    "zz": {
        "role": "运维",
        "age": 24,
        "password": "passwd"
    }
}

@app.post("/api/login")
async def login(id:str, password: str, db: Session = Depends(get_db))->LoginInfo:
    from utils.token import generate_token
    if id not in users_db or users_db[id]["password"] != password:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    token = generate_token(id)
    return LoginInfo(token= token, id=id)

@app.post("/api/login1/{id}/shabi/{path:path}") 
async def bestexample(
    user:User, # Pydantic的东西都是body里发送的。
    id:int, # 默认的平凡类型就是query里发送
    path:Annotated[str,Path(min_length=10,max_length=20,regex="^fixedquery$")], # validation用法。 Path代表path参数。
    item:Item,
    qq: Annotated[str | None, Query(alias="item-query")] , # 所谓的Alias Parameters。你想用“/items/?item-query=foobaritems”，但item-query毕竟不是合法的python变量。这样就能拧过来。
    qq1: Annotated[str | None, Query(deprecated=True)] , # 指定这个变量要被抛弃了。这样在Swagger UI里会有醒目的红色提示。
    hidden_query: Annotated[str | None, Query(include_in_schema=False)], # 可以从schema中消失，进而在Swagger UI里你也看不见他。
    q:Annotated[str,Query(title="Query string",description="Query string for the items to search in the database that have a good match")], # 可以加入更多的元信息。
    qqq:list[str] = ["foo", "bar"], # list的query参数是啥意思，意思就是类似于“/items/?q=foo&q=bar”的东西。带默认参数的意思就是如果访问“/items/”，它照样给你[foo,bar].
    needy:int|None=..., # 这个...代表必须。虽然你可以None，但就算None也得显式发过来
    needy2:int|None=Required, # 也可以用Pydantic.Required表示必须。
    desc:str|None=None, # =None代表可选参数
    short:bool=False # 带默认值也表示是可选参数。注意对于Boolean，主要判断query字符串是yes, on, True, true, Yes, On这几个。只要是这几个都算True，其他的就归类为False。
    )->LoginInfo:
    return LoginInfo(token= "token", name="sb")

@app.post("/api/logout")
async def logout(credentials: Annotated[HTTPBasicCredentials, Depends(security)])->None:
    if not verify_token(credentials.credentials):
        raise HTTPException(status_code=401, detail="未授权的访问")
    return {}

import crud
import schemas

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/users/me")
def get_my_detail(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    db: Session = Depends(get_db)
    ):
    return crud.get_current_user_detail(db, token=credentials.credentials)

# 写好了，别改。
@app.get("/tickets")
def get_all_tickets(skip: int = 0, limit: int = 100,db: Session = Depends(get_db))->list[schemas.TicketBrief]:
    return crud.get_tickets(db,skip=skip,limit=limit)

# 写好了，别改。
@app.post("/tickets")
def create_ticket(tc:schemas.TicketCreate, 
                  credentials: Annotated[HTTPBasicCredentials, Depends(security)],
                  db: Session = Depends(get_db))->schemas.TicketCreateSuccess:
    from utils.token import get_user_id_from_token
    user_id=get_user_id_from_token(credentials.credentials)
    t = crud.create_ticket(db, user_id=user_id,tc=tc)
    return t # orm模式打开了，它会自动转换的。

# 写好了，别改。
@app.get("/tickets/{ticket_id}")
def get_one_tickets(ticket_id:int,db: Session = Depends(get_db))->schemas.TicketDetail:
    return crud.get_ticket_detail(db,ticket_id)

# 写好了，别改。
@app.post("/tickets/{ticket_id}")
def edit_one_tickets(te:schemas.TicketEdit,db: Session = Depends(get_db)):
    crud.edit_ticket(db=db,te=te)

# 写好了，别改。
@app.get("/ticket_types")
def get_ticket_types():
    return crud.get_ticket_types()

# security = HTTPBasic()


# @app.get("/users/me")
# def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
#     return {"username": credentials.username, "password": credentials.password}

def verify_token(token: str) -> bool:
    # verify the JWT token
    return True

