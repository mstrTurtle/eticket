from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

#正常登录
def test_user():
    params = {'id': 0, 'password': 'passwd'}
    response = client.post("/api/login",params=params)
    assert response.status_code == 200

#用户不存在时的登录
def test_no_user():
    params = {'id': 999, 'password': 'passwd'}
    response = client.post("/api/login",params=params)
    assert response.status_code == 404

#登陆时密码错误
def test_error_password():
    params = {'id': 0, 'password': 'passwdx'}
    response = client.post("/api/login",params=params)
    assert response.status_code == 401

#正常登录再登出
def test_logout_auth():
    params = {'id': 0, 'password': 'passwd'}
    response = client.post("/api/login",params=params)
    assert response.status_code == 200
    token = response.json()['token']
    response = client.post("/api/logout",headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 200


#未登录时调用登出功能
def test_logout_unauth():
    response = client.post("/api/logout")
    assert response.status_code == 403
