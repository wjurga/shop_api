
def test_create_store(store):
    assert store is not None


def test_create_store_detail(store):
    assert store.name == 'store_name'