#!/usr/bin/python3
"""
Lists all State objects from the hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Create a configured "session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Query the database
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()
