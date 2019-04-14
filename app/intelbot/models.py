from sqlalchemy import Column, Integer, TEXT
from app import Base
from app import engine


class FunnyStuff(Base):
    __tablename__ = "funnystuff"
    __bind_key__ = 'reddit_database_comments'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    comment = Column(TEXT)


class FoodStuff(Base):
    __tablename__ = "foodstuff"
    __bind_key__ = 'reddit_database_comments'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    comment = Column(TEXT)


class Subs(Base):
    __tablename__ = "subs"
    __bind_key__ = 'reddit_database_comments'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True)
    datestamp = Column(TEXT)
    Parent_ID = Column(TEXT)


class WhoMSg(Base):
    __tablename__ = "message"
    __bind_key__ = 'reddit_database_comments'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True)
    datestamp = Column(TEXT)
    subreddit = Column(TEXT)
    username = Column(TEXT)


Base.metadata.create_all(engine)
