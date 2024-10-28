# fast_api.py

from fastapi import FastAPI

app = FastAPI(title="Concord API", version="1.0")


@app.get("/")
def read_root():
    return {"message": "Welcome to Concord API"}
