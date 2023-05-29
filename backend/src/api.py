from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Required

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated, Optional

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 设置CORS中间件
origins = [
    "http://localhost",
    "http://localhost:8080"
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
    name: str
    password: str

class LoginInfo(BaseModel):
    token:str
    name:str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

users_db = {
    "turtle": {
        "age": 24,
        "password": "passwd"
    }
}

@app.post("/api/login")
async def login(name:str, password: str)->LoginInfo:
    if name not in users_db or users_db[name]["password"] != password:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    token = generate_token(name)
    return LoginInfo(token= token, name=name)

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




# security = HTTPBasic()


# @app.get("/users/me")
# def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
#     return {"username": credentials.username, "password": credentials.password}

def generate_token(email: str) -> str:
    # generate JWT token based on the user's email address
    return "dummy_token"

def verify_token(token: str) -> bool:
    # verify the JWT token
    return True

