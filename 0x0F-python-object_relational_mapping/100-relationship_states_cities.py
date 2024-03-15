#!/usr/bin/python3
"""
Script that creates the State `California` with the City
`San Francisco` from the database hbtn_0e_100_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username, password, database_name = sys.argv[1:4]

    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database_name), pool_pre_ping=True)

    # Creating all tables in the engine
    Base.metadata.create_all(engine)

    # Creating new session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Creating California
    california = State(name="California")
    session.add(california)
    session.flush()

    # Creating San Francisco
    san_francisco = City(name="San Francisco", state_id=california.id)
    session.add(san_francisco)
    # Commiting changes
    session.commit()
    # Closing session
    session.close()
