#!/usr/bin/python3
'''Prints State object with the name passed as arg'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = [row.id for row in session.query(State).
              filter(State.name == sys.argv[4])]
    if result:
        for e in result:
            print(e)
    else:
        print("Not found")
    session.close()
