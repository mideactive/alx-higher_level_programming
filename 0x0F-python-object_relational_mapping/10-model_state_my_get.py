#!/usr/bin/python3
"""Script that prints state object with name as argument passed to it"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
         sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    query = session.query(State).filter(State.name.like(sys.argv[4]))
    for instance in query:
        print("{}".format(instance.id))
    if (len(query.all()) == 0):
        print("Not found")
    session.close()
