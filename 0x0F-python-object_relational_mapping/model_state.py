#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3],
        sys.argv[4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
