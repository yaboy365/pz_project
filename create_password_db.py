from sqlalchemy import create_engine, MetaData, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Credentials(Base):
    __tableName__ = 'credentials'
    login = Column(String, primary_key=True)
    password = Column(String)
    premissions = Column(String)

    def __repr__(self):
        return "<Credentials(login='%s', password='%s', premissions='%s')>" % (
            self.login, self.password, self.premissions)


def create():
    engine = create_engine('sqlite:///credentials.db', echo=True)

    meta = MetaData()

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    # session = sessionmaker(bind=engine)
    session.add_all([
        Credentials(login='lekarz', password='lekarz', premissions='lekarz'),
        Credentials(login='admin', password='admin', premissions='admin'),
        Credentials(login='pielegniarka', password='pielegniarka', premissions='pielegniarka')
    ])
    Credentials.__table__.create(bind=engine)
    session.commit()
