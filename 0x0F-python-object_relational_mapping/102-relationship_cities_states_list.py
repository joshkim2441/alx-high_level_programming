#!/usr/bin/python3
"""
List all City objects from the hbtn_0e_101_usa database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_nname = sys.argv[3]

    # Create engine that connects to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (username, password, db_nname), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Query the database for all states, joined with cities
    # ordered by stattes.id and cities.id
    for state in session.query(State).all():
        for city in state.cities:
            print("{}: {} -> {}".format(city.id,
                                        city.name, state.name))
    # Close session
    session.close()
