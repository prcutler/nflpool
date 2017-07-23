import mongoengine
import nflpool.data.mongo_setup as mongo_setup


class Account(mongoengine.Document):
    first_name = mongoengine.StringField(required=True)
    last_name = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True)
    phone = mongo.engine.IntField()
    twitter = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'users,'
    }