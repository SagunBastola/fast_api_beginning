from pydantic import BaseModel
from typing import List,Dict,Optional
from pydantic import Field
class Cart(BaseModel):
    user_id:int
    items:List[str]
    quantity:Dict[str,int]
    image_url:Optional[str]=None
class Employee(BaseModel):
    id : int
    name: str=Field(...,min_length=3,description="Employee Name", example="Ganesh")
    department: Optional[str] = None
    salary: float=Field(...,ge=10000)
employee1=Employee(id=1,name="Ganesh",department="IT",salary=50000)
print(employee1)
