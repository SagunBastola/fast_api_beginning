from pydantic import BaseModel

class userdata(BaseModel):
    id: int
    name: str
    is_active: bool
dict1={"id":1,"name":"ganesh", "is_active":True}
user1=userdata(**dict1)
print(user1)

class product(BaseModel):
    id : int
    name : str
    price : int
    in_stock: bool = True
dict2={"id":1,"name":"Mobile","price":1000}
product1=product(**dict2)
print(product1)