#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Querying the first State object
    first_state = session.query(State).order_by(State.id).first()
    # Displaying result
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    # Closing session
    session.close()
