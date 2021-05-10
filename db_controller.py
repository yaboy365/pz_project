import sqlite3

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float, MetaData, Table, delete, text
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


def print_rooms():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    r = c.execute("SELECT * FROM Room")
    for row in r:
        print(row)


def print_patient():
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
    metadata = MetaData()
    tab_db = Table('Patient', metadata, autoload=True, autoload_with=engine)

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

    """
    def read(self, element_id):
        query = select([self.tab_db]).where(self.tab_db.columns.id == element_id)
        with self.engine.begin() as connection:
            result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        print(result_set)
    """

    def read_patient(self, element):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        r = c.execute("SELECT * FROM Patient WHERE id == " + str(element))
        for row in r:
            return row

    def delete_patient(self, element):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        r = c.execute("DELETE FROM Patient  WHERE id == " + str(element))

    """
    def delete(self, element):
        query = delete([self.tab_db]).where(self.tab_db.columns.id == element)
        self.session.delete(query)
        self.session.commit()
    """

    def clear_patients(self):
        print("Are you sure about that?\n1 - Yes\n2 - No")
        x = int(input())
        if x == 1:
            with self.engine.connect() as connection:
                result = connection.execute(text("DELETE FROM Patient"))
        else:
            print("Quiting...")

    def get(self):
        print('xd')
