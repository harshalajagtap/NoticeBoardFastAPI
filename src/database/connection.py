from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

# create engine
engine = create_engine("postgresql://postgres:12345678@localhost/fastapi")

# session creation
session_local = sessionmaker(autoflush=False, autocommit=False)

# configure above session
session_local.configure(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
