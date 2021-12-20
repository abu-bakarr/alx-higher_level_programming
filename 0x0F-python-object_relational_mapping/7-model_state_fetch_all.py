#!/usr/bin/python3
"""
List all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":

    # Create engine. The args comes from input
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
   
    states = session.query(State).order_by(State.id)
   
    for state in states:
        print("{}: {}".format(state.id, state.name))
