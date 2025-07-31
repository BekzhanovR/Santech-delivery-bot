from sqlalchemy import Column, Integer, String
from utils.db_api.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    name = Column(String)
    surname = Column(String)
    phone = Column(String)
    region = Column(String)
    city = Column(String)
    # role = Column(String)  # "ish_beruvchi" yoki "ish_qidiruvchi"
    profession = Column(String, nullable=True)  # ish izlash uchun

class JobRequest(Base):
    __tablename__ = "job_requests"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    description = Column(String)
    time = Column(String)
    needed_profession = Column(String)
