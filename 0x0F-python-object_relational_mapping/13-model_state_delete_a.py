#!/usr/bin/python3
"""
Deletes all State objects with a name containing the
letter 'a' from the hbtn_0e_6_usa database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_nname = sys.argv[3]

    # Create engine that connects to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (username, password, db_nname), pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Query database for states with names containig
    # the letter 'a'
    states = session.query(State).filter(State.name.contains('a'))

    for state in states:
        session.delete(state)
    # Commit the session
    session.commit()
    # Close the session
    session.close()
