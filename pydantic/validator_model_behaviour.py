from pydantic import BaseModel, field_validator,model_validator,computed_field
from pydantic import Field
class User(BaseModel):
    username: str
    
    @field_validator("username")
    def validate_username(cls,value):
        if len(value)<3:
            raise ValueError("Invalid")
        return value
user1=User(username="Ganesh")
print(user1)

class password(BaseModel):
    password: str
    confirm_password: str
    
    @model_validator(mode="after")
    def validates(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("Not valid password")
        return values
Dict3={"password":"New", "confirm_password":"New"}
passwor=password(**Dict3)
class product(BaseModel):
    name: str
    price: int
    
    @computed_field
    @property
    def discounted_price(self)->float:#new field is created of discounted price with float
        return self.price*0.9
product1=product(name="Mobile", price=1000)
print(product1)
class supermarket(BaseModel):
    name : str = Field(...,min_length=3,description="Supermarket Name",example="Big Bazzar")
    password: str
    confirm_password: str
    
    @model_validator(mode="after")
    def validate(cls,values):
        if(values.password != values.confirm_password):
            raise ValueError("NOT valiD PASSWORD")
        return values
    
    income: float
    @field_validator("income")
    def validate(cls,v):
        if v<0 or v>100000 :
            raise ValueError("No in the bracket")
    
    total : float
    @computed_field
    @property
    def discounted_price(self)->float :
        return self.total*0.9;
supermarket1=supermarket(name="Big Bazzar", password="Ganesh", confirm_password="Ganesh", income=50000, total=100000)
print(supermarket1)
