#!/usr/bin/python3
"""
Script to list all State objects from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    # Creating engine to connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)

    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Querying and sorting all State objects by id
    states = session.query(State).order_by(State.id).all()
    # Displaying results
    for state in states:
        print("{}: {}".format(state.id, state.name))
    # Closing session
    session.close()
