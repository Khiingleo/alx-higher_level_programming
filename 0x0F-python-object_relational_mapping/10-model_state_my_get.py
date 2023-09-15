#!/usr/bin/python3
"""
prints the State object with the 'name' passed as argumment from
the database
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user, passwd, db = argv[1], argv[2], argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(user, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()

    if state is not None:
        print(state.id)
    else:
        print("Not found")

    session.close()
