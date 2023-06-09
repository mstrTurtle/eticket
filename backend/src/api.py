from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Required

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated, Optional

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from schemas import TicketType
from utils.token import TokenError, parse_token

from model.base import Base,engine,SessionLocal,memory_mode
from sqlalchemy.orm import Session
from model.populate import populate

Base.metadata.create_all(engine)

if memory_mode:
    print("mem")
    populate()

# https://stackoverflow.com/questions/63762387/how-to-group-fastapi-endpoints-in-swagger-ui
tags_metadata = [
    {"name": "0 Auth", "description": "认证相关接口"},
    {"name": "1 User", "description": "用户相关接口"},
    {"name": "2 Ticket", "description": "表单相关接口"},
]

# https://fastapi.tiangolo.com/tutorial/metadata/
app = FastAPI(
    title='ETICKET API Doc',
    description='这是ETICKET工单系统的后端API的文档, 同时它可以方便调试。步骤：先登录，拿到token加进HTTP头的Authentication，再操作。',
    version="0.9.0",
    openapi_tags=tags_metadata
    )

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
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

# https://www.51cto.com/article/707542.html

@app.middleware("http")
async def log_requests(request, call_next):
    from logger import logger
    import random
    import string
    import time
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    
    return response

security = HTTPBearer()

class LoginInfo(BaseModel):
    token:str
    id:str


@app.post("/api/login", tags=["0 Auth"])
async def 登录(id:int, password: str, db: Session = Depends(get_db))->LoginInfo:
    from utils.token import generate_token
    from utils.hash import hash
    # if id not in users_db or users_db[id]["password"] != password:
    #     raise HTTPException(status_code=401, detail="用户名或密码错误")
    u = crud.get_user(db,user_id=id)
    if not u :
        raise HTTPException(status_code=404, detail="User not found")
    if u.hashed_password != hash(password=password):
        print("pswd")
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    token = generate_token(id)
    return LoginInfo(token= token, id=id)

@app.post("/api/logout", tags=["0 Auth"])
async def 登出(credentials: Annotated[HTTPBasicCredentials, Depends(security)])->None:
    try:
        verify_token(credentials.credentials)
    except TokenError as e:
        raise HTTPException(406,str(e))
import crud
import schemas


@app.get("/users/me", tags=["1 User"])
def 获取当前用户详情(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    db: Session = Depends(get_db)
    )->schemas.UserDetail:
    '''
    获取当前用户详细信息
    '''
    try:
        return crud.get_current_user_detail(db, token=credentials.credentials)
    except TokenError as e:
        raise HTTPException(406,str(e))

# 写好了，别改。
@app.get("/tickets", tags=["2 Ticket"])
def 获取所有工单(skip: int = 0, limit: int = 100,db: Session = Depends(get_db))->list[schemas.TicketBrief]:
    '''
    获取所有的工单
    '''
    return crud.get_tickets(db,skip=skip,limit=limit)

# 写好了，别改。
@app.post("/tickets", tags=["2 Ticket"])
def 新建工单(tc:schemas.TicketCreate, 
                  credentials: Annotated[HTTPBasicCredentials, Depends(security)],
                  db: Session = Depends(get_db))->schemas.TicketCreateSuccess:
    '''
    创建一个新工单
    '''
    try:
        from utils.token import get_user_id_from_token
        user_id=get_user_id_from_token(credentials.credentials)
        t = crud.create_ticket(db, user_id=user_id,tc=tc)
        return t # orm模式打开了，它会自动转换的。
    except KeyError as e:
        raise HTTPException(404,str(e))
    except TokenError as e:
        raise HTTPException(406,str(e))

# 写好了，别改。
@app.get("/tickets/{ticket_id}", tags=["2 Ticket"])
def 获取某工单详情(ticket_id:int,db: Session = Depends(get_db))->schemas.TicketDetail:
    '''
    获取某工单的详细信息
    '''
    try:
        return crud.get_ticket_detail(db,ticket_id)
    except KeyError as e:
        raise HTTPException(404,str(e))

# 写好了，别改。
@app.post("/tickets/{ticket_id}", tags=["2 Ticket"])
def 修改某工单(te:schemas.TicketEdit,db: Session = Depends(get_db)):
    '''
    修改某个工单
    '''
    try:
        crud.edit_ticket(db=db,te=te)
    except KeyError as e:
        raise HTTPException(404,str(e))

# 写好了，别改。
@app.get("/ticket_types", tags=["2 Ticket"])
def 获取所有可用工单类型()->list[TicketType]:
    '''
    获取所有能创建的工单类型
    '''
    return crud.get_ticket_types()

@app.get("/notifications", tags=["3 Noti"])
def 获取通知列表() -> list[str]:
    '''
    获取通知列表
    '''
    return ['请各单位注意','请各单位落实好通知']


@app.post("/api/login1/{id}/shabi/{path:path}", tags=["9 Example"]) 
async def 一个简单的例子(
    loginInfo:LoginInfo, # Pydantic的东西都是body里发送的。
    id:int, # 默认的平凡类型就是query里发送
    path:Annotated[str,Path(min_length=10,max_length=20,regex="^fixedquery$")], # validation用法。 Path代表path参数。
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
    '''
    一个简单生动的例子
    '''
    return LoginInfo(token= "token", name="sb")


def verify_token(token: str) -> bool:
    # verify the JWT token
    parse_token(token)
    return True

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)