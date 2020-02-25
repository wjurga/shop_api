
def test_create_user(user):
    assert user is not None


def test_create_user_detail(user):
    assert user.username == 'user_name'
    assert user.password == 'password'