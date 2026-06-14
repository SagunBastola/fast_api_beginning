from fastapi import FastAPI, HTTPException, status

app=FastAPI()
@app.get("/")
def root():
    return {"message":"Welcome"}
@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message":"User_Created"}

@app.get("/user")
def get_user():
    return {
        "status":"sucess", #we can also send custom response http code
        "message":"User Fetched",
        "data":{
            "name":"sagun",
            "age":12
            }    
        }

@app.get("/user/{user_id}")
def get_user(user_id : int):
    if user_id != 1 :
        raise HTTPException(
            status_code=404,
            detail="User Not found"
        )
    else:
        return {"user_name":"sagun"}