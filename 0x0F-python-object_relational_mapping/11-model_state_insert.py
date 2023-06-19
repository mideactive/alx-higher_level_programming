#!/usr/bin/python3

"""A script that adds a new state object to the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:\
            {}@localhost/{}'
            .format(sys.argv[1] ,sys.argv[2] ,sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)

    session.commit()

    query = session.query(State).filter(State.name.like('Louisiana'))
    for instance in query:
        print("{}".format(instance.id))
    session.close()
