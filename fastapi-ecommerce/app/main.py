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
def list_products(name: str = 
                  Query(default= None,min_length=1,max_length=50,description="search product by name: "),
                  sort_by_price: bool=Query(default=False,description="sort products by price"),
                  order : str = Query(default="asc",description="when sort_by_price is true sort by (asc/dsc)"),
                  limit : int =Query(default=4,description="no of items to be viewed")):
    products=get_all_products()
    if name: 
        needle = name.strip().lower()
        products=[p for p in products if needle in p.get("name").lower()]
        if not products:
            raise HTTPException(status_code=404,detail="product not found")
    if sort_by_price:
        reverse =(order == "dsc")
        products=sorted(products,reverse=reverse,key=lambda p: p.get("price",""))
    total=len(products)
    products=products[0:limit]
    return {"total":total,"products":products}