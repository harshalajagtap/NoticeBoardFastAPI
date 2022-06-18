from pydantic import BaseModel
from datetime import date


class NoticePost(BaseModel):
    date: date
    applicable_for: str
    title: str
    notice: str
