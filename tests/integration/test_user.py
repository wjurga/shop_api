from shop_restapi.models.user import UserModel


def test_user_not_exist(app):
    assert not UserModel.find_by_id(1)
    assert not UserModel.find_by_username('test_user')


def test_user_save_to_db_find_by_username(app, user):
    user.save_to_db()

    assert UserModel.find_by_username('test_user')


def test_user_save_to_db_find_by_id(app, user):
    user.save_to_db()

    assert UserModel.find_by_id(1)


def test_delete_user(app, user):
    user.save_to_db()
    user.delete_from_db()

    assert not UserModel.find_by_username('test_user')