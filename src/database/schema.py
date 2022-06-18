from pydantic import BaseModel
from datetime import date


class NoticePost(BaseModel):
    date: date
    applicable_for: str
    title: str
    notice: str


class NoticeGet(BaseModel):
    date: date
    applicable_for: str
    title: str
    notice: str

    class Config:
        orm_mode = True


class NoticePut(BaseModel):
    id: int
    date: date
    applicable_for: str
    title: str
    notice: str


