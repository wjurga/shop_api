import pytest
from shop_restapi.models.item import ItemModel
from shop_restapi.models.store import StoreModel
from shop_restapi.models.user import UserModel


@pytest.fixture
def item():
    item = ItemModel(name='item_name', price=1.00, store_id=1)
    return item


@pytest.fixture
def store():
    store = StoreModel(name='store_name')
    return store


@pytest.fixture
def user():
    user = UserModel(username='user_name', password='password')
    return user
