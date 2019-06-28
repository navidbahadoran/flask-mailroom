import os

from peewee import Model, CharField, IntegerField, ForeignKeyField
from playhouse.db_url import connect
from login import login_manager
from flask_login import UserMixin

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///new_database.db'))


@login_manager.user_loader
def load_user(user_id):
    query = Donor.select().where(Donor.id == int(user_id))
    if query:
        return query.get()
    else:
        return None


class Donor(Model, UserMixin):
    username = CharField(unique=True)
    name = CharField()
    password = CharField()

    class Meta:
        database = db


class Donation(Model):
    value = IntegerField()
    donor = ForeignKeyField(Donor, backref='donations')

    class Meta:
        database = db
