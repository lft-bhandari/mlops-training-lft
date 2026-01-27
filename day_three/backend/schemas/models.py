from sqlalchemy import Column, Integer, String, Text
from database.db import Base

class UserTask(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    designation = Column(String(100), nullable=False)
    tasks = Column(Text, nullable=False)
