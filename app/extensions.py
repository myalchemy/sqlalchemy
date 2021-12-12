from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

session = scoped_session(sessionmaker())
Base = declarative_base()