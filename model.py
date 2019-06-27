import os

from peewee import Model, CharField, IntegerField, ForeignKeyField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///new_database.db'))


class Donor(Model):
    username = CharField(max_length=20, unique=True)
    name = CharField(max_length=20)
    password = CharField(max_length=20)

    class Meta:
        database = db


class Donation(Model):
    value = IntegerField()
    donor = ForeignKeyField(Donor, backref='donations')

    class Meta:
        database = db
