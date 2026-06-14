from fastapi import FastAPI,Depends,Header,HTTPException

app = FastAPI()

def verify_token(token: str = Header(None)):#header is mostly used of token / password sending for security purposes
    if token != "mysecrettoken":
        raise HTTPException(status_code=404,detail="Unauthorized")
    return {"message":"User Authorized"}

@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return {"message":"secured",
            "message":user}


# def comman_logic():
#     return {
#         "message":"common logic exceuted"
#     }

# @app.get("/home")
# def home(data = Depends(comman_logic)):
#     return data