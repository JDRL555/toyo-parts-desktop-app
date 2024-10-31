from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

engine = create_engine(os.environ.get("SQLALCHEMY_URI"))
Session = sessionmaker(engine)

session = Session()
Base = declarative_base()