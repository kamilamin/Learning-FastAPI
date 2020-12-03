from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"message": "Hello world."}

@app.get("/component/{component_id}") # Path Parameter
def view_component(component_id: int):
    return {"Component_ID": component_id}

@app.get('/component/')
def get_component(number: int, text: str):
    return {"Number": number, "Text": text}
