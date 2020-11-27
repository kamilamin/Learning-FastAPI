from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

db = []

class City(BaseModel):
    name: str
    timezone: str

@app.get('/')

def read_root():
    return {'Hello': 'world'}

@app.get('/cities')
def get_cities():
    results = []
    for city in db:
        r = requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
        print(r)
        current_time = r.json()['datetime']
        print(current_time)
        results.append({'name': city['name'], 'timezone': city['timezone'], 'current_time': current_time})
    return results

@app.get('/cities/{city_id}')
def get_city(city_id: int):
    return db[city_id-1]

@app.post('/addNewcity')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]

@app.delete('/cities')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}
