
from fastapi import FastAPI
import uvicorn
from src.api.v1.NoticeBoardRouter import nb_router


app = FastAPI()         # creating instance
app.include_router(nb_router, prefix="/api/v1")

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)




