#!/usr/bin/python3
""" Base class and states class definition.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey


class City(Base):
    """ City class that defines the cities table.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
