from flask_security import UserMixin
from peewee import BooleanField, DateTimeField, TextField

from ..db import db

Model = db.Model


class User(Model, UserMixin):
    class Meta:
        table_name = 'users'

    active = BooleanField(default=False)
    admin = BooleanField(default=False)
    confirmed_at = DateTimeField(null=True)
    email = TextField(unique=True)
    password = TextField()
