from pydantic import BaseModel, field_validator,model_validator,computed_field
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