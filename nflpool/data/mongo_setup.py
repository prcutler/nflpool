import mongoengine


# Don't forget to pass in production values; server, username, pw, etc
def global_init():
    mongoengine.register_connection(alias="core", name="nflpool")