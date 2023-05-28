from fastapi import FastAPI, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

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
    id: int
    email: str

users_db = {
    "a@b.com": {
        "id": 123,
        "password": "password"
    }
}

@app.post("/api/login")
async def login(user: dict):
    email = user["email"]
    password = user["password"]
    if email not in users_db or users_db[email]["password"] != password:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    token = generate_token(email)
    return {"message": "登录成功", "data": {"token": token, "user": users_db[email]}}

@app.post("/api/logout")
async def logout(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if not verify_token(credentials.credentials):
        raise HTTPException(status_code=401, detail="未授权的访问")
    return {"message": "注销成功"}




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

