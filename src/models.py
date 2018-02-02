from sqlalchemy import Column, Integer, Text
from db import Base


class Builds(Base):
    __tablename__ = 'builds'
    id = Column(Integer, primary_key=True)
    time_stamp = Column(Text)
    build_log = Column(Text)
    build_status = Column(Integer)

    def __init__(self, time_stamp=None, build_log=None, build_status=0):
        self.time_stamp = time_stamp
        self.build_log = build_log
        self.build_status = build_status

    def __repr__(self):
        return '<Build %r>' % self.time_stamp
