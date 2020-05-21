import logging
from configparser import ConfigParser, ExtendedInterpolation
from sqlalchemy.types import PickleType, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import engine_from_config, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.schema import UniqueConstraint


Base = declarative_base()
logger = logging.getLogger('face_recognition.database')
config_parser = ConfigParser(interpolation=ExtendedInterpolation())
config_parser.read('config.ini')


class Celeb(Base):
    """
    """
    __tablename__ = 'celeb_recognition_encodings'

    celeb_id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)
    encodings = Column(PickleType, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            'name', 'encodings', name='_celeb_encodings_unique'
    ),)

    def __repr__(self):
        return "<Celeb(celeb_id='{celeb_id}', name='{name}')>".format(
            celeb_id=self.celeb_id, name=self.name
        )


def get_engine_and_session_factory():
    """
    To start talking to the database, the ORM’s “handle” to the
    database is the Session. create a session-factory which will
    serve as a factory for new Session objects and the engine to
    connect to the database. (Should be called only once per
    database (postgresql) during whole program's execution)
    :return: engine-  * Engine has not actually tried to connect
    to the database yet; that happens only the first time it is
    asked to perform a task against the database., session-factory.
    """

    # CHANGE TO READ CONFIG FROM SQLALCHEMY_POSTGRES IF WORKING WITH POSTGRES-DB
    engine = engine_from_config(config_parser['SQLALCHEMY_SQLITE'])

    # Other transactional characteristics may be
    # defined when calling sessionmaker
    Session = sessionmaker(bind=engine)

    return engine, Session


class Operations(object):

    ENGINE, session_factory = get_engine_and_session_factory()

    @staticmethod
    def get_new_session():
        """
        gets a new session from the session factory, registers
        the hstore on the new session's connection registering
        hstore enable the interaction with a dictionary type column
        of the database.
        :return: a new session object which are bound to our database.
        """
        session = None
        session = Operations.session_factory()
        return session

    @staticmethod
    def get_celebs():
        session = Operations.get_new_session()
        celebs = session.query(Celeb)

        session.close()

        return celebs

    @staticmethod
    def add_celeb(name, encodings):
        celeb_id = None
        session = Operations.get_new_session()
        celebrity = Celeb(name=name, encodings=encodings)
        session.add(celebrity)

        try:
            session.flush()
        except Exception as e:
            logger.error(e)
            session.rollback()
        else:
            celeb_id = celebrity.celeb_id
            session.commit()
        finally:
            session.close()

        return celeb_id

    @staticmethod
    def create_tables():
        Base.metadata.create_all(Operations.ENGINE)
