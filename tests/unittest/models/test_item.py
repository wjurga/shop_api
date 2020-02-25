
def test_create_item(item):
    assert item is not None


def test_create_item_detail(item):
    assert item.name == 'item_name'
    assert item.price == 1.00
    assert item.store_id == 1


