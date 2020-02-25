import pytest
from shop_restapi import create_app
from shop_restapi.db import db
from config import TestConfig
from shop_restapi.models.store import StoreModel
from shop_restapi.models.item import ItemModel


@pytest.fixture
def app():
    app = create_app(TestConfig)

    with app.app_context():
        db.init_app(app)
        db.create_all()
        yield app
        db.session.remove()
        db.session.close()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def item(app):
    item = ItemModel(name='item_name', price=10.01, store_id=1)
    return item


@pytest.fixture
def store(app):
    store = StoreModel(name='store_name')
    return store
