#!/usr/bin/python3
"""
Script to add the State object "Louisiana" to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieving command line arguments
    username, password, database = sys.argv[1:4]
    # Creating engine to connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
    # Binding engine with Base class
    Base.metadata.create_all(engine)
    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Creating State object for "Louisiana"
    new_state = State(name="Louisiana")
    # Adding State object to the session
    session.add(new_state)
    # Committing changes to the database
    session.commit()
    # Printing the new states.id after creation
    print(new_state.id)
    # Closing session
    session.close()
