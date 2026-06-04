from itertools import product

from fastapi import FastAPI, HTTPException, Query
from service.product import get_all_products
app=FastAPI()

@app.get("/")
def root():
    return {"message":"welcome to the website"}

# @app.get("/products/{id}")
# def get_product(id:int):
#     product=["shoe","light","mobile","pen","pencil"]
    
#     return product[id]



# @app.get("/products")
# def get_product(id:int):
#     return get_all_products()


@app.get("/products")
def list_products(name: str = Query(default= None,min_length=1,max_length=50,description="search product by name: ")):
    products=get_all_products()
    if name: 
        needle = name.strip().lower()
        products=[p for p in products if needle in p.get("name").lower()]
        if not products:
            raise HTTPException(status_code=404,detail="product not found")
        total=len(products)
    return {"total":total,"products":products}