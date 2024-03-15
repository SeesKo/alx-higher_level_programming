#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Creating engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creating session to interact with database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Querying database to get all State objects and
    # their corresponding City objects
    states = session.query(State).order_by(State.id).all()

    # Printing the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    # Closing the session
    session.close()
