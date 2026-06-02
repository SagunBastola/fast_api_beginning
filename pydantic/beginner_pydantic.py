from pydantic import BaseModel
from typing import Optional
class Student(BaseModel):
    name: str
    age: int
std={"name":"ganesh","age":'12'}
st=Student(**std)
print(st)

class User(BaseModel):
    name: str
    email: Optional[str] = None
ut=User(name="ganesh")
print(ut)

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True
pd=Product(name="ganesh",price=123.34)
print(pd)