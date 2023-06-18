#!/usr/bin/python3
""" A script that lists all states from hbtn_0e_6_usa db"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database):
    """Lists all State objects from the database hbtn_0e_6_usa."""
    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and display the states
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
