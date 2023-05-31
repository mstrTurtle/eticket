from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

#正常登陆时获取用户信息
def test_users_me():
    params = {'id': 0, 'password': 'passwd'}
    response = client.post("/api/login",params=params)
    assert response.status_code == 200
    token = response.json()['token']

    response = client.get("/users/me",headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 200

#未登陆时获取用户信息
def test_users_me_unauth():
    response = client.get("/users/me")
    assert response.status_code == 403

#token错误
def test_error_token():
    token = 'xxx'

    response = client.get("/users/me",headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 200