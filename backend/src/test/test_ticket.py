from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

token='eyJpc3MiOiAidHVydGxlIiwgInN1YiI6IDAsICJleHAiOiAxNjg1NTU3MTY3LjY2OTAwOX0='
headers={"Authorization": f'Bearer {token}'}

#获取所有工单信息
def test_tikets():
    response = client.get("/tickets")
    assert response.status_code == 200

def test_tikets_post():
    params = {'skip': 200, 'limit': -1}
    response = client.get("/tickets",params=params)
    assert response.status_code == 200

def test_tikets_post1():
    params = {'skip': -1, 'limit': 200}
    response = client.get("/tickets",params=params)
    assert response.status_code == 200

#正常创建新工单
def test_tikets_create():
    params1 = {'id': 0, 'password': 'passwd'}
    response = client.post("/api/login",params=params1)
    assert response.status_code == 200

    json = {'ticket_type_id': 1, 'title': 'test_title'}
    response = client.post("/tickets",json=json,headers=headers)
    assert response.status_code == 200

#未登录时创建新工单
def test_no_user_create():
    json = {'ticket_type_id': 1, 'title': 'test_title'}
    response = client.post("/tickets",json=json)
    assert response.status_code == 403