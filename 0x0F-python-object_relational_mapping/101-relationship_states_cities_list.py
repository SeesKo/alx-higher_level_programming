#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    # Creating the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all State objects
    states = session.query(State).order_by(State.id).all()

    # Printing State and corresponding City objects
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # Closing the session
    session.close()
