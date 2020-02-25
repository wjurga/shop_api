from shop_restapi.models.store import StoreModel


def test_save_to_db(store):
    assert not StoreModel.find_by_name('store_name')
    store.save_to_db()

    assert StoreModel.find_by_name('store_name')


def test_delete_from_db(store):
    store.save_to_db()
    store.delete_from_db()

    assert not StoreModel.find_by_name('store_name')


def test_create_store_items_empty(store):
    store.save_to_db()
    assert not store.items.all()


def test_store_relationship(item, store):
    store.save_to_db()
    item.save_to_db()
    items = StoreModel.find_by_name('store_name').items
    assert items.count() == 1


def test_find_all_with_no_item(app):
    stores = StoreModel.find_all()
    assert len(stores) == 0


def test_find_all(store):
    store.save_to_db()

    stores = StoreModel.find_all()

    assert len(stores) == 1

