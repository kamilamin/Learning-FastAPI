from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Package(BaseModel):
    name: str
    number: int
    description: Optional[str]

app = FastAPI();

@app.get("/")
def index():
    return {"Message": "Hello World"}

@app.post("/package/{priority}")
def make_package(priority: int, package: Package, value: bool):
    return {"priority": priority, **package.dict(), "value": value}