from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse

app=FastAPI()
#custom exception

class UserNotfound(Exception):
    def __init__(self,name: str):
        self.name=name

        
@app.exception_handler(UserNotfound)
def user_not_found(request : Request , ex:UserNotfound):
    return JSONResponse(status_code=404,content={"status":"error"})

@app.get("/user/{name}")
def get_user(name : str):
    if name != "sagun" :
        raise UserNotfound(name)
    return {"name":name}


# @app.get("/user/{user_id}")
# def get_user(user_id : int):
#     if(user_id != 1):
#         raise HTTPException(status_code=404,detail="Not Found")
#     return {"message":"sucess"}