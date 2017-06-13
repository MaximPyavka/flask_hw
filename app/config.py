import os

dev_config = {
    "DEBUG": True,
    "SECRET_KEY": 'my_secret_key',
    "BASE_DIR": os.path.dirname(os.path.abspath(__file__))
}


prod_config = {
    "DEBUG": False,
    "SECRET_KEY": 'my_prod_secret_key',
}

test_config = {
    "DEBUG": True,
    "SECRET_KEY": 'my_test_secret_key',
}
