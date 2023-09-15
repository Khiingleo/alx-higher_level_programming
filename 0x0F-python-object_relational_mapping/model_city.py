#!/usr/bin/python3
"""
Defines a class City
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """
    inherits from Base
    links to the MySQL table "cities"
    """

    __tablename__ = "cities"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
