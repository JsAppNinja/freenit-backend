import os
from importlib import import_module

import pytest
from config import configs
from name import app_name
from peewee_migrate import Router
from peewee_migrate.router import DEFAULT_MIGRATE_DIR
from pytest_factoryboy import register

from .factories import AdminFactory, RoleFactory, UserFactory

application = import_module(f'{app_name}')

register(UserFactory)
register(AdminFactory)
register(RoleFactory)


@pytest.fixture
def app():
    config = configs['testing']
    flask_app = application.create_app(config)
    router = Router(
        flask_app.db.database,
        migrate_dir=f'{DEFAULT_MIGRATE_DIR}/main',
    )
    #  log_router = Router(
    #      flask_app.logdb.database,
    #      migrate_dir=f'{DEFAULT_MIGRATE_DIR}/logs',
    #  )
    router.run()
    #  log_router.run()
    yield flask_app
    flask_app.db.close_db('')
    #  flask_app.logdb.close_db('')
    current_path = os.path.dirname(__file__)
    os.remove('{}/../test.db'.format(current_path))
    #  os.remove('{}/../log_test.db'.format(current_path))
