#!/usr/bin/python3
"""
Print the State object with the name passed as argument
from the hbtn_0e_6_usa database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_nname = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine that connects to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (username, password, db_nname), pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Query database for the first state
    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
    # Close the session
    session.close()
