#!/usr/bin/python3
"""
Creates the State 'California' with the City
'San Francisco' from the hbtn_0e_100_usa database
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
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Create new State object
    new_state = State(name="California")
    # Create new City object
    new_city = City(name="San Francisco")
    # Add the new city to the state's cities
    new_state.cities.append(new_city)
    # Add the new state to the session
    session.add(new_state)
    # Commit the transaction
    session.commit()
    # Close the session
    session.close()
