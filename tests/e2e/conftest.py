import pytest
import json

from shop_restapi.models.user import UserModel


@pytest.fixture
def access_token(client, app):
    UserModel(username='test_user', password='1234').save_to_db()
    auth_resp = client.post('/login',
                            data=json.dumps({'username': 'test_user', 'password': '1234'}),
                            headers={'Content-type': 'application/json'})
    auth_token = json.loads(auth_resp.data)['access_token']
    return f'Bearer {auth_token}'


