from fastapi import APIRouter

nb_router = APIRouter()


@nb_router.get("/notice")
def myname(a, b=0):
    return int(a)+int(b)




