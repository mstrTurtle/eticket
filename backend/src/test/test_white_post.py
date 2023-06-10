import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from api import app
from api import 登录 as login

import ticket_type.yunwei as yunwei
import api 


client = TestClient(app)



# 测试postHandler逻辑覆盖
def test_yunwei1():
    s="后勤"
    # M={'驳回':True}
    M = {}
    assert yunwei.postHandler(s,M) == ('领导',M)
    ...
def test_yunwei2():
    s="领导"
    M={'驳回':True}
    assert yunwei.postHandler(s,M) == ('后勤',M)

def test_yunwei3():
    s="领导"
    M={'驳回':False}
    assert yunwei.postHandler(s,M) == ('运维',M)

def test_yunwei4():
    s="运维"
    M={}
    assert yunwei.postHandler(s,M) == ('归档',M)

def test_yunwei5():
    s="错误"
    M={}
    try:
        yunwei.postHandler(s,M)
        assert False
    except Exception as e:
        assert str(e) == '有问题的状态'
    except BaseException :
        assert False
    
def test_login1():
    id=0
    password='passwd'
    from utils.token import generate_token
    token = generate_token(id)
    db = next(api.get_db())
    linfo = asyncio.run( api.登录(id,password,db))
    assert type(linfo) is api.LoginInfo
    
def test_login2():
    id=999
    password='passwd'
    db = next(api.get_db())
    try:
        assert asyncio.run(api.登录(id,password,db))
        assert False
    except HTTPException as e:
        assert  e.status_code == 404
    except BaseException :
        assert False

def test_login3():
    id=0
    password='wrong'
    db = next(api.get_db())
    try:
        assert asyncio.run(api.登录(id,password,db))
        assert False
    except HTTPException as e:
        assert  e.status_code == 401
    except BaseException :
        assert False