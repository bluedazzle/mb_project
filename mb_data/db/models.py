# coding: utf-8

from __future__ import unicode_literals

from sqlalchemy import Column, String, DateTime, Integer, Boolean, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ICOProject(Base):
    __tablename__ = 'core_ico_project'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    logo = Column(String)
    status = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)


