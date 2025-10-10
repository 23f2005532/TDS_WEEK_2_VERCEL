# api/index.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello, Jules!"}
