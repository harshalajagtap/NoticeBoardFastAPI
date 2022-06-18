from sqlalchemy import Integer, Column, DateTime, String
from src.database.connection import Base


class NoticeBoard(Base):
    __tablename__ = "notice_board"
    __table_args__ = {"schema": "nb_schema"}
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=True)
    applicable_for = Column(String(255), nullable=True)
    title = Column(String(255), nullable=False)
    notice = Column(String(2550), nullable=False)


