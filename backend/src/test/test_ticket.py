from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

token='eyJpc3MiOiAidHVydGxlIiwgInN1YiI6IDAsICJleHAiOiAxNjg1NTU3MTY3LjY2OTAwOX0='
headers={"Authorization": f'Bearer {token}'}

#获取所有工单信息
def test_all_tikets():
    response = client.get("/tickets")
    assert response.status_code == 200

#测试超出限制的范围对获取的影响
def test_limit_num():
    params = {'skip': 200, 'limit': -1}
    response = client.get("/tickets",params=params)
    assert response.status_code == 200

#测试反向输入范围约束数字的影响
def test_another_limit():
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

#登录失败时创建新工单
def test_tikets_create_nologin():
    params1 = {'id': 3131, 'password': 'passwd'}
    response = client.post("/api/login",params=params1)
    assert response.status_code == 404

    json = {'ticket_type_id': 99, 'title': 'test_title'}
    response = client.post("/tickets",json=json)
    assert response.status_code == 403

#登录失败时创建新工单
def test_tikets_create_loginfail():
    params1 = {'id': 1, 'password': 'asdhauds'}
    response = client.post("/api/login",params=params1)
    assert response.status_code == 401

    json = {'ticket_type_id': 99, 'title': 'test_title'}
    response = client.post("/tickets",json=json)
    assert response.status_code == 403

#创建不存在类型的新工单
def test_tikets_create_error():
    params1 = {'id': 0, 'password': 'passwd'}
    response = client.post("/api/login",params=params1)
    assert response.status_code == 200

    json = {'ticket_type_id': 99, 'title': 'test_title'}
    response = client.post("/tickets",json=json,headers=headers)
    assert response.status_code == 404

#正常获取工单详情
def test_tickets_detail():
    ticket_id=1
    response = client.get(f"/tickets/{ticket_id}")
    assert response.status_code == 200

#获取不存在的工单详情
def test_tickets_error():
    ticket_id=99
    response = client.get(f"/tickets/{ticket_id}")
    assert response.status_code == 404


#正常修改工单
def test_change_tiket():
    json = {'id': 1, 'form_model': 'string'}
    ticket_id=1
    response = client.post(f"/tickets/{ticket_id}",json=json)
    assert response.status_code == 200

#不正常修改工单
def test_change_another_tiket():
    json = {'id': 199, 'form_model': 'string'}
    ticket_id=1
    response = client.post(f"/tickets/{ticket_id}",json=json)
    assert response.status_code == 404

#正常获取可用的工单类型
def test_tikets_type():
    response = client.get("/ticket_types")
    assert response.status_code == 200