from my_package import HOW_TO_SAY_GOODBYE

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"This is what I want to say": HOW_TO_SAY_GOODBYE}
