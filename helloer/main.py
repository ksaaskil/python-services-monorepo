from my_package import HOW_TO_SAY_HELLO

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"This is what I want to say": HOW_TO_SAY_HELLO}
