#!/usr/bin/python3
"""
Prints all City objects from the hbtn_0e_14_usa database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

# Create engine that connects to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (username, password, db_name), pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Query the database for all cities, joined with states,
    # ordered by cities.id
    for city, state in session.query(City, State)\
            .join(State).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    # Close session
    session.close()
