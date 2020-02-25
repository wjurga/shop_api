import json
from shop_restapi.models.store import StoreModel


def test_create_store(client):
    resp = client.post('/store/store_name')

    assert resp.status_code == 201
    assert json.loads(resp.data) == {'id': 1, 'name': 'store_name', 'items': []}
    assert StoreModel.find_by_name('store_name')


def test_create_duplicate_store(client):
    client.post('/store/store_name')

    resp = client.post('/store/store_name')

    assert resp.status_code == 400
    assert json.loads(resp.data) == {'message': "A store with name 'store_name' already exists."}


def test_delete_store(client, store):
    store.save_to_db()

    resp = client.delete('/store/store_name')

    assert resp.status_code == 200
    assert not StoreModel.find_by_name('store_name')
    assert json.loads(resp.data) == {'message': 'Store deleted.'}


def test_find_store(client, store):
    store.save_to_db()

    resp = client.get('/store/store_name')

    assert resp.status_code == 200
    assert json.loads(resp.data) == {'id': 1, 'name': 'store_name', 'items': []}


def test_store_not_found(client):
    resp = client.get('/store/store_name')

    assert resp.status_code == 404
    assert json.loads(resp.data) == {'message': 'Store not found.'}


def test_store_found_with_items(client, store, item):
    store.save_to_db()
    item.save_to_db()

    resp = client.get('/store/store_name')

    assert resp.status_code == 200
    assert json.loads(resp.data) == {'id': 1,
                                     'name': 'store_name',
                                     'items': [{'id': 1, 'name': 'item_name', 'price': 10.01, 'store_id': 1}]}


def test_store_list(client, store):
    store.save_to_db()

    resp = client.get('/stores')

    assert json.loads(resp.data) == {'stores': [{'id': 1, 'name': 'store_name', 'items': []}]}


def test_store_list_with_items(client, store, item):
    store.save_to_db()
    item.save_to_db()

    resp = client.get('/stores')

    assert json.loads(resp.data) == {'stores':
        [
            {'id': 1,
             'name': 'store_name',
             'items': [{'id': 1, 'name': 'item_name', 'price': 10.01, 'store_id': 1}]}
        ]
    }
