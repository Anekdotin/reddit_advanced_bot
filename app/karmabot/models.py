

from sqlalchemy import Column, Integer, TEXT
from app import Base2
from app import engine2


class Bots(Base2):
    __tablename__ = "users"
    __bind_key__ = 'reddit_database_users'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(TEXT)
    password = Column(TEXT)
    appname = Column(TEXT)
    client_id = Column(TEXT)
    client_secret = Column(TEXT)
    user_agent = Column(TEXT)
    post_count = Column(Integer)


Base2.metadata.create_all(engine2)
