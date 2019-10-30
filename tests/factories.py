from importlib import import_module

import factory
from flask_security.utils import hash_password
from name import app_name

auth = import_module(f'{app_name}.models.auth')


class UserFactory(factory.Factory):
    class Meta:
        model = auth.User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.LazyAttribute(lambda a: hash_password('Sekrit'))
    username = factory.Faker('name')
    active = True


class AdminFactory(UserFactory):
    admin = True


class RoleFactory(factory.Factory):
    class Meta:
        model = auth.Role

    name = factory.Faker('first_name')
