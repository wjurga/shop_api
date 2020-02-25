import json


def test_get_item_not_found(client):
    resp = client.get('item/test')

    assert resp.status_code == 404


def test_get_item(client, item, store):
    store.save_to_db()
    item.save_to_db()

    resp = client.get('item/item_name')

    assert resp.status_code == 200


def test_put_item(client, item, store):
    store.save_to_db()
    item.save_to_db()

    resp = client.put('item/item_name',
                      data=json.dumps({'price': 9.99, 'store_id': 1}),
                      headers={'Content-type': 'application/json'})

    assert resp.status_code == 200
    assert json.loads(resp.data) == {'id': 1, 'name': 'item_name', 'price': 9.99, 'store_id': 1}


def test_put_not_exist_item(client):
    resp = client.put('item/item_new',
                      data=json.dumps({'price': 9.99, 'store_id': 1}),
                      headers={'Content-type': 'application/json'})

    assert resp.status_code == 200
    assert json.loads(resp.data) == {'id': 1, 'name': 'item_new', 'price': 9.99, 'store_id': 1}


def test_delete_not_exist_item(client, access_token):
    resp = client.delete('item/item_name', headers={'Authorization': access_token})

    assert resp.status_code == 404
    assert json.loads(resp.data) == {'message': 'Item deleted.'}


def test_delete_item(client,item, store, access_token):
    store.save_to_db()
    item.save_to_db()

    resp = client.delete('item/item_name', headers={'Authorization': access_token})

    assert resp.status_code == 200
    assert json.loads(resp.data) == {'message': 'Item deleted.'}


def test_create_item(client, store, access_token):
    store.save_to_db()
    resp = client.post('item/item_name',
                       data=json.dumps({'price': 10.01, 'store_id': 1}),
                       headers={'Authorization': access_token, 'Content-type': 'application/json'})

    assert resp.status_code == 201
    assert json.loads(resp.data) == {'id': 1, 'name': 'item_name', 'price': 10.01, 'store_id': 1}


def test_create_duplicate_item(client, item, store, access_token):
    store.save_to_db()
    item.save_to_db()

    resp = client.post('item/item_name',
                       data=json.dumps({'price': 9.99, 'store_id': 1}),
                       headers={'Authorization': access_token, 'Content-type': 'application/json'})

    assert resp.status_code == 400
    assert json.loads(resp.data) == {'message': "An item with name 'item_name' already exists."}



