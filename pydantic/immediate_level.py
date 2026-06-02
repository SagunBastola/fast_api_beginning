from pydantic import BaseModel,Field,EmailStr
from typing import List,Optional,Dict

class Course(BaseModel):
    title: str
    students: List[str]
cd=Course(
    title="Python",
    students=["Ram", "Shyam", "Hari"]
)
print(cd)

class Address(BaseModel):
    city: str
    country: str
class User(BaseModel):
    name: str
    address: Address
ut=User(name="Ganesh",address=Address(city="tokyo",country="Japan"))
print(ut)

class Person(BaseModel):
    name: str
    email: EmailStr
pa=Person(name="Ganesh",email="ganesh@gmail.com")
print(pa)

class User_world(BaseModel):
    username: str = Field(...,min_length=3)
    password: str = Field(...,max_length=8)
pa=User_world(username="ganesh",password="abcd0f")
print(pa)

class Market(BaseModel):
    name: str
    price: float = Field(...,ge=0)
ma=Market(name="ganesh",price=22000)
print(ma)
    