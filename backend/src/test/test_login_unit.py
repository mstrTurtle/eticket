import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from api import app
from api import 登录 as login

import api

def test_login_info_id():
    id=0
    password='passwd'
    from utils.token import generate_token
    token = generate_token(id)
    db = next(api.get_db())
    linfo = asyncio.run( api.登录(id,password,db))
    assert linfo.id == id


def test_login_info_token():
    id=0
    password='passwd'
    from utils.token import generate_token
    token = generate_token(id)
    db = next(api.get_db())
    linfo = asyncio.run( api.登录(id,password,db))
    assert linfo.token == token