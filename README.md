
# SHOP_API - example of using Flask to build REST API

### To start the application, perform the following actions. 

Create directory.
```
mkdir shop_api
cd shop_api
```
Clone repo from GitHub.
```
git clone https://github.com/wjurga/shop_api.git .
```

Install the necessary packages.
```
python3 -m venv venv
pip install -r requirements.txt
```
Activate virtual environment.
```
source venv/bin/activate
```
Prepare environment variables.
```
cp .env.example .env
nano .env
```

Run tests.
```
pytest
```
You should see:
```
collected 46 items

tests/e2e/test_item.py ........                                                         [ 17%]
tests/e2e/test_store.py ........                                                        [ 34%]
tests/e2e/test_user.py ...                                                              [ 41%]
tests/integration/test_item.py .....                                                    [ 52%]
tests/integration/test_store.py ......                                                  [ 65%]
tests/integration/test_user.py ....                                                     [ 73%]
tests/unittest/models/test_item.py ..                                                   [ 78%]
tests/unittest/models/test_store.py ..                                                  [ 82%]
tests/unittest/models/test_user.py ..                                                   [ 86%]
tests/unittest/schemas/test_item.py ..                                                  [ 91%]
tests/unittest/schemas/test_store.py ..                                                 [ 95%]
tests/unittest/schemas/test_user.py ..                                                  [100%]

===================================== 46 passed in 2.44s ======================================

```
Prepare your database.
```
flask db upgrade
```
Run app.
```
flask run
```