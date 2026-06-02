from pydantic import BaseModel, field_validator,model_validator,computed_field,EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    age: int
    
    @field_validator("age")
    def validate(cls,a):
        if(a < 18):
            raise ValueError("age is not greater than 18")
        
        return a
    @field_validator("password")
    def valid(cls,p):
        if len(p) < 8:
            raise ValueError("not enough password length")
        return p
ut=User(username="ganesh",email="ganesh@gmail.com",password="new_is_enough",age=18)
print(ut)