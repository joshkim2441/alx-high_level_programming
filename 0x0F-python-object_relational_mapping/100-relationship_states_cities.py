#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

# Get credentials from environment variables (assuming they are set)
username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
database_name = os.environ.get('DB_NAME')

# Construct connection URL using environment variables
DATABASE_URL = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}'

def create_state_city(session):
  """Creates the State "California" with the City "San Francisco" """
  newState = State(name="California")
  newCity = City(name="San Francisco", state=newState)
  session.add(newState)
  session.add(newCity)
  session.commit()

if __name__ == "__main__":
  engine = create_engine(DATABASE_URL, pool_pre_ping=True)
  Base.metadata.create_all(engine)
  Session = sessionmaker(bind=engine)

  try:
    session = Session()
    create_state_city(session)
    print("State and City created successfully!")
  except Exception as e:
    print(f"An error occured: {e}")
  finally:
    session.close()  # Always close the session
