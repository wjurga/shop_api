import json
from shop_restapi.schemas.store import StoreSchema


def test_store_to_json(store):
    store_schema = StoreSchema()
    assert store_schema.dump(store) == {'id': None, 'items': [], 'name': 'store_name'}


def test_store_from_json():
    store_schema = StoreSchema()
    json_data = json.dumps({'name': 'store_name'})

    new_store = store_schema.loads(json_data)

    assert new_store.name == 'store_name'

