import sys
from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, TEXT, BLOB
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class AmityRooms(Base):
    __tablename__ = 'Rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_name = Column(String(20), nullable=False)
    room_type = Column(String(20), nullable=False)

class Persons(Base):
    __tablename__ = 'People'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(15), nullable=False)
    lname = Column(String(15), nullable=False)
    person_identifier = Column(Integer, nullable=False)
    role = Column(String(20), nullable=False)
    office_allocated = Column(String(20), nullable=True)
    living_allocated = Column(String(20), nullable=True)

def create_db(db_name):
    engine = create_engine('sqlite:///' + db_name)
    Base.metadata.create_all(engine)
    return engine
