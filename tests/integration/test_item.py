from shop_restapi.models.item import ItemModel


def test_save_to_db(item):
    assert not ItemModel.find_by_name('item_name')
    item.save_to_db()

    assert item.find_by_name('item_name')


def test_delete_from_db(item):
    item.save_to_db()
    item.delete_from_db()

    assert not ItemModel.find_by_name('item_name')


def test_store_relationship(item, store):
    store.save_to_db()
    item.save_to_db()

    assert ItemModel.find_by_name('item_name').store.name == 'store_name'


def test_find_all_with_no_item(app):
    items = ItemModel.find_all()

    assert len(items) == 0


def test_find_all(item):
    item.save_to_db()

    items = ItemModel.find_all()

    assert len(items) == 1