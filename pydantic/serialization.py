from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id : int
    name: str
    email: str
    is_active: bool = True
    created: datetime
    
    address:Address
    tags:List[str]=[]
    
    
user = User(id=1,
            name="sagun",
            email="sagunbastola@gmail.com",
            created=datetime(2015,2,12),
            address=Address(
                street="new_Street",
                city="new_City",
                zip_code="12321"
            ),
            tags=["new_is_the_way","old_is_the_way"]
        )
print(user)
print("=======================================")
data_dict=user.model_dump()
print(data_dict)
print("==========================")
json_data=user.model_dump_json()
print(json_data)
print("================================")