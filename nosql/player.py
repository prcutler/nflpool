import mongoengine


class Player(mongoengine.EmbeddedDocument):
    firstname = mongoengine.StringField(required=True)
    lastnane = mongoengine.StringField(required=True)
    twitter = mongoengine.StringField()
    email = mongoengine.StringField(required=True)

    # TODO: Add all player fields including pick categories
