from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI_0, SQLALCHEMY_DATABASE_URI_1


# session one is info
# engine 1
engine = create_engine(SQLALCHEMY_DATABASE_URI_0)
Base = declarative_base()
Base.metadata.reflect(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# session 2 is users
# engine 2
engine2 = create_engine(SQLALCHEMY_DATABASE_URI_1)
Base2 = declarative_base()
Base2.metadata.reflect(bind=engine2)
Session2 = sessionmaker(bind=engine2)
session2 = Session2()
