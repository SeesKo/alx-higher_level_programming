#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
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
    # Querying and deleting states with name containing 'a'
    states_to_delete = session.query(State)\
        .filter(State.name.like('%a%'))\
        .all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()
