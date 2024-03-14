#!/usr/bin/python3
"""
Script to print the State object with the name passed
as argument from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:5]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Querying State object with the given name
    state = session.query(State).filter(State.name == state_name).first()
    # Displaying result
    if state:
        print(state.id)
    else:
        print("Not found")
    # Closing session
    session.close()
