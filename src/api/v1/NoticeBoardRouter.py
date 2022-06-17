from fastapi import APIRouter


nb_router = APIRouter()


@nb_router.get("/notice")
def get_notice(rdate):
    return {"date": rdate, "notice": "This is first notice"}


@nb_router.post("/notice")
def add_notice(rdate,applicable_for, title, notice):
    return {"date": rdate, "applicable_for": applicable_for, "title": title, "notice":notice }

@nb_router.put("/notice")
def add_notice(notice_id, rdate, applicable_for, title, notice):
    return {"notice_id":notice_id, "date": rdate, "applicable_for": applicable_for, "title": title, "notice":notice }


@nb_router.delete("/notice")
def delete_notice(notice_id):
    return {"notice_id": f"notice {notice_id} has been deleted"}




