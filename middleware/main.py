from fastapi import FastAPI,Request
import time

app=FastAPI()
@app.middleware("http")
async def logging(request : Request,call_next):
    start=time.time()
    response = await call_next(request)
    end=time.time()
    print(f"path : {request.url.path} | time: {end-start}")
    return response
# @app.middleware("http")
# async def my_middleware(request : Request,call_next) :
#     print("Request Received")
    
#     response = await call_next(request)

#     print("Requesst Sent")

#     return response