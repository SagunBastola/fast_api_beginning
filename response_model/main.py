from fastapi import FastAPI
import fastapi
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name: str
    age : int
    password : str

class UserResponse(BaseModel):
    name : str
    age : int

@app.get("/user",response_model=UserResponse)
def get_user():
    return {"name":"sagun",
            "age":12,
            "password":"sdfjsad"}