import sqlite3

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Room(Base):
    __tablename__ = 'Room'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=True)
    size = Column(Integer, nullable=False)

    patient = relationship("Patient", backref="Room")

    def __init__(self, number, size):
        self.number = number
        self.size = size


class Patient(Base):
    __tablename__ = 'Patient'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    temp_max = Column(Float)
    temp_min = Column(Float)
    room = Column(Integer, ForeignKey('Room.id'))

    def __init__(self, name, surname, temp_max, temp_min, room):
        self.name = name
        self.surname = surname
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.room = room


def printRooms():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    r = c.execute("SELECT * FROM Room")
    for row in r:
        print(row)


def printPatient():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    r = c.execute("SELECT * FROM Patient")
    for row in r:
        print(row)


class DBController:
    engine = create_engine("sqlite:///database.db", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        """
        engine = create_engine("sqlite:///database.db", echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        """

    def add(self, element):
        self.session.add(element)
        self.session.commit()
