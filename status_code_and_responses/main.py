from fastapi import FastAPI, status

app=FastAPI()
@app.get("/")
def root():
    return {"message":"Welcome"}
@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message":"User_Created"}