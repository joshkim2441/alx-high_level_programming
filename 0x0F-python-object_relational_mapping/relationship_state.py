#!/usr/bin/python3
"""
Python file containing class definition of a State
and instance Base = declarative_base().
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm  import relationship

Base = declarative_base()


class State(Base):
    """ The State class that inherits from Base """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
