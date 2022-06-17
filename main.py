
from fastapi import FastAPI
import uvicorn

app = FastAPI()         # creating instance

@app.get('/blog')
def myname(a, b=0):
    return int(a)+int(b)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


