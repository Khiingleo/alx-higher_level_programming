#!/usr/bin/python3
"""
list all City objects from the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    user, passwd, db = argv[1], argv[2], argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(user, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
