import json


def test_register_user(client):
    resp = client.post('/register',
                       data=json.dumps({'username': 'user_name', 'password': 'password'}),
                       headers={'Content-type': 'application/json'})
    assert resp.status_code == 201
    assert json.loads(resp.data) == {"message": "User created successfully."}


def test_register_and_login(client):
    client.post('/register',
                data=json.dumps({'username': 'user_name', 'password': 'password'}),
                headers={'Content-type': 'application/json'})
    resp = client.post('/login',
                       data=json.dumps({'username': 'user_name', 'password': 'password'}),
                       headers={'Content-Type': 'application/json'})
    assert 'access_token' in json.loads(resp.data).keys()


def test_register_duplicate_user(client):
    client.post('/register',
                data=json.dumps({'username': 'user_name', 'password': 'password'}),
                headers={'Content-type': 'application/json'})
    resp = client.post('/register',
                       data=json.dumps({'username': 'user_name', 'password': 'password'}),
                       headers={'Content-type': 'application/json'})

    assert resp.status_code == 400
    assert json.loads(resp.data) == {"message": "A user with that username already exists."}
