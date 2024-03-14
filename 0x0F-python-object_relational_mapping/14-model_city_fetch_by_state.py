#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit()

    username, password, database = sys.argv[1:4]

    # Creating the engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
    # Binding the engine to the session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Querying and printing all City objects by state
    cities = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
