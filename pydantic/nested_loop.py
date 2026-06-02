from typing import List,Optional
from pydantic import BaseModel

class Address(BaseModel):
    country: str
    postal_code: str
class User(BaseModel):
    id : int
    name: str
    address: Address
add1=Address(country="Nepal",postal_code="29384")
user1=User(id=1,name="Ganesh",address=add1)
print(user1)

class Comment(BaseModel):
    id : int
    content: str
    replies: Optional[list['Comment']]= None
Comment.model_rebuild() # to resolve the forward reference
comment1=Comment(id=1,content="This is a comment")
comment2=Comment(id=2,content="This is a reply",replies=[comment1])
print(comment2)

class Lesson(BaseModel):
    id : int
    content: str
class Module(BaseModel):
    id_module : int
    content: str
    lessons:List[Lesson]
class Course(BaseModel):
    id_course: int
    content: str
    modules:List[Module]
lesson1=Lesson(id=1,content="This is a lesson")

module1=Module(id_module=1,content="This is a module",lessons=[lesson1])
course1=Course(id_course=1,content="This is a course",modules=[module1])
print(course1)
