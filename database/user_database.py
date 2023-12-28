from datetime import datetime
from sqlalchemy import String, Column, Integer, DateTime, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from models.user_model import UserModel

_engine = create_engine("sqlite:///apidatabase.db", echo=True)
Session = scoped_session(sessionmaker(bind=_engine))

Base = declarative_base()

"""
    UserDatabase:
        id int
        userId String
        email String
        password String
        datatime Datatime    
"""


class UserDatabase(Base):
    __tablename__ = "userdb"
    id = Column(Integer(), primary_key=True)
    userId = Column(String())
    email = Column(String())
    password = Column(String())
    datatime = Column(DateTime(), default=datetime.utcnow())

    def __init__(self, user_model: UserModel):
        self.email = user_model.email
        self.password = user_model.password
        self.userId = user_model.userId

    def __repr__(self):
        return f'''
        UserDatabase(
            id={self.id},
            userId={self.userId},
            email={self.email},
            password={self.password},
            datatime={self.datatime}
        )
        '''


Base.metadata.create_all(bind=_engine)
_session = sessionmaker(bind=_engine)
Session = _session()
