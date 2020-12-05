from fastapi import FastAPI
from fastapi_cloudauth.cognito import CognitoCurrentUser
from pycognito import Cognito
from pydantic import BaseModel

u = Cognito('us-east-1_TWOFHGEu2', '1sbge6ar88q1o9a7g2s976dbac')

# u.set_base_attributes(email='kamil@live.com', some_random_attr='abc123')

# u.register('kamil@live.com', 'Kamil.000')
# print(u)


app = FastAPI()

class SignUpModel(BaseModel):
    email: str
    password: str

@app.get('/')
def index():
    return {"Message": "Hello world"}


@app.post("/signup")
def signup(signup: SignUpModel):
    u.register(signup.email, signup.password)
    print(u)
    return "hello"

# @app.post("/login")
# def login(username: str, email: str, password: str):
#     return {"username": username, "email": email, "password": password}
