import json
from shop_restapi.schemas.item import ItemSchema


def test_item_to_json(item):
    item_schema = ItemSchema()
    assert item_schema.dump(item) == {'id': None, 'name': 'item_name', 'price': 1.00, 'store_id': 1}


def test_item_from_json():
    item_schema = ItemSchema()
    json_data = json.dumps({'name': 'item_name', 'price': 1.00, 'store_id': 1})

    new_item = item_schema.loads(json_data)

    assert new_item.name == 'item_name'
    assert new_item.price == 1.00
    assert new_item.store_id == 1