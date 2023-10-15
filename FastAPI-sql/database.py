from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DATABASE = "sqlite:///./finance.db"

engine = create_engine(URL_DATABASE, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# is a factory function that constructs a base class for declarative class definitions
# https://docs.sqlalchemy.org/en/14/orm/extensions/declarative/api.html#sqlalchemy.ext.declarative.declarative_base
