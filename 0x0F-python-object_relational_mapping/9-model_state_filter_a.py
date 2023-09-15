#!/usr/bin/python3
"""
lists all State objects that contain the letter 'a'
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    user, passwd, db = argv[1], argv[2], argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(user, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    session.close()
