#!/usr/bin/python3
""" A script that lists all states from hbtn_0e_6_usa db"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == '__main__':
    h = 'localhost'
    u = sys.argv[1]
    pas = sys.argv[2]
    db_n = sys.argv[3]
    p = 3306
    eng = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
          u, pas, h, p, db_n))

    Session = sessionmaker(bind=eng)
    session = Session().query(State).order_by(State.id)
    for state in session:
        print("{}: {}".format(state.id, state.name))
