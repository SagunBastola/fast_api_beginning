from tkinter import W

from pydantic import BaseModel, field_validator, model_validator, HttpUrl

class User(BaseModel):
    name: str
    age: int 
    
    @field_validator("age")
    def validate(cls,v):
        if v<18 :
            raise ValueError("age must be greater than 18")
        return v
    
ut=User(name="ganesh",age=22)
print(ut)

class Register_user(BaseModel):
    name : str
    password : str
    confirm_password : str
    @model_validator(mode="after")
    def validate(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("Password_doesn't match")
        return values
rt=Register_user(name="ganesh",password="hello", confirm_password="hello")
print(rt)

class Web(BaseModel):
    url:HttpUrl
w=Web(url="https://www.google.com")
print(w)