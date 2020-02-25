import json
from shop_restapi.schemas.user import UserSchema


def test_store_to_json(user):
    user_schema = UserSchema()
    assert user_schema.dump(user) == {'id': None, 'username': 'user_name'}


def test_store_from_json():
    user_schema = UserSchema()
    json_data = json.dumps({'username': 'user_name', 'password': 'password'})

    new_user = user_schema.loads(json_data)

    assert new_user.username == 'user_name'
    assert new_user.password == 'password'
