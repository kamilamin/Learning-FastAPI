from fastapi import FastAPI
from fastapi_cloudauth.cognito import CognitoCurrentUser
# from pycognito import Cognito
# from aws_cdk.aws_cognito import CfnUserPoolGroup

app = FastAPI()

@app.get('/')
def index():
    return {"Message": "Hello world"}

@app.post("/login")
def login(username: str, email: str, password: str):
    return {"username": username, "email": email, "password": password}