from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Tickets(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    data = Column(Date, index=True, nullable=False)
    theatre_name = Column(String(255), index=True, nullable=False)
    performance_name = Column(String(255), index=True, nullable=False)
    tickets_count = Column(Integer, index=True, nullable=False)


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True, nullable=False, unique=True)
    password_hash = Column(String(255), index=True, nullable=False)
