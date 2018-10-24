from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, create_engine

Base = declarative_base()


class DataAccessLayer:
    def __init__(self):
        self.engine = None
        self.Session = None
        self.session = None
        self.conn_string = "sqlite:////test_nflpooldb.sqlite"

    def connect(self):
        self.engine = create_engine(self.conn_string)
        Base.metadata.bind = self.engine
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)


dal = DataAccessLayer()
