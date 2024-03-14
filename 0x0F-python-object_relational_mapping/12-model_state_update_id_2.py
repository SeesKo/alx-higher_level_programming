#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
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
    # Querying and updating the state
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
    session.close()
