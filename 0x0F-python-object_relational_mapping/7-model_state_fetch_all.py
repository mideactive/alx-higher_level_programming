#!/usr/bin/python3
""" A script that lists all states from hbtn_0e_6_usa db"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    un = sys.argv[1]
    pw = sys.argv[2]
    dt = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@locahost:3306/{}'
            .format(un, pw, dt))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and display the states
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
