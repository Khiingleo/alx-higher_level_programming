#!/usr/bin/python3
"""
Defines a class State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    inherits from Base
    Linked to MySQL table 'states'
    """
    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
