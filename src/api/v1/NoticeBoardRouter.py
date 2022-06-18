from fastapi import APIRouter
from src.database.schema import NoticePost

nb_router = APIRouter()


@nb_router.get("/notice")
def get_notice(nid: int = None):
    return {"noticeid": nid}


@nb_router.post("/notice")
def add_notice(req: NoticePost):
    return req


@nb_router.put("/notice")
def add_notice(notice_id, rdate, applicable_for, title, notice):
    return {"notice_id":notice_id, "date": rdate, "applicable_for": applicable_for, "title": title, "notice":notice }


@nb_router.delete("/notice")
def delete_notice(notice_id):
    return {"notice_id": f"notice {notice_id} has been deleted"}




