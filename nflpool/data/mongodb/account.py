import datetime
import mongoengine


class Account(mongoengine.Document):
    first_name = mongoengine.StringField(required=True)
    last_name = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True, unique=True)
    phone = mongoengine.IntField()
    twitter = mongoengine.StringField()
    created = mongoengine.DateTimeField(default=datetime.datetime.now)
    super_user = mongoengine.BooleanField(default=False)
    password_hash = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'users,'
    }