from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session

from src.database.connection import get_db
from src.database.schema import NoticePost, NoticeGet, NoticePut
from src.database.models import NoticeBoard as notice_tb


nb_router = APIRouter()


@nb_router.get("/notice")
def get_notice(nid: int = None,  db: Session = Depends(get_db)):
    res = db.query(notice_tb).filter(notice_tb.id == nid).first()

    return NoticeGet.from_orm(res)


@nb_router.post("/notice")
def add_notice(req: NoticePost, db: Session = Depends(get_db)):
    record = notice_tb(**req.dict())
    db.add(record)
    db.commit()
    return req.dict()


@nb_router.delete("/notice")
def delete_notice(nid: int, db: Session = Depends(get_db)):
    record = db.query(notice_tb).filter(notice_tb.id == nid).first()
    db.delete(record)
    db.commit()
    return {"notice_id": f"notice {nid} has been deleted"}


@nb_router.put("/notice")
def update_notice(req: NoticePut, db: Session = Depends(get_db)):
    db.query(notice_tb).filter(notice_tb.id == req.id).update(req.dict())
    db.commit()
    return {"id": req.id, "result": "updated"}







