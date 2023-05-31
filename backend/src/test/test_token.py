from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

#正常登出，应该校验token
def test_token_invalid():

    token = 'xxx'
    response = client.post("/api/logout",headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 406 

#无token新建工单
def test_token_create():
    
    token = 'xxx'
    json = {'ticket_type_id': 1, 'title': 'test_title'}
    response = client.post("/tickets",json=json,headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 406