import pytest

from shop_restapi.models.user import UserModel


@pytest.fixture
def user(app):
    user = UserModel(username='test_user', password='1234')
    return user
