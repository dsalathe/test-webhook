from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import models

engine = create_engine('sqlite:///../database.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """
    Database initialization
    :return:
    """
    Base.metadata.create_all(bind=engine)
    create_build("This is a test message", False)


def create_build(log, status):
    """
    Creates a new build entry in the database. Generates the time stamp
    :param log: The log file from the build
    :param status: The status of the build. False for fail and True for success.
    :return:
    """
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    b = models.Builds(time_stamp, log, int(status))
    db_session.add(b)
    db_session.commit()
