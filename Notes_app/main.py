from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Welcome to my notes application"

@app.get("/name")
def name():
    return "Meghaj"