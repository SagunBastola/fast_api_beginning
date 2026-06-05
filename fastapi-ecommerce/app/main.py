from fastapi import FastAPI, HTTPException, Query , Path
from service.product import get_all_products,add_products,delete_product
from schema.product import Product
from uuid import uuid4,UUID
from datetime import datetime

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





@app.get("/products/{product_id}")
def product_based_on_id(product_id : str = Path(...,max_length=36,min_length=36,examples=list("0005a4ea-ce3f-4dd7-bee0-f4ccc70fea6a"),description="Product id of 36 characters")):
    products=get_all_products()
    product=[p for p in products if p.get("id","") == product_id]
    if not product:
        raise HTTPException(status_code=404,detail="error found!!!")
    return {"product_id": product_id , "product" : product}


@app.post("/products",status_code=201)
def create_products(product: Product):
    product_dict=product.model_dump(mode="json")
    product_dict["id"]=str(uuid4())
    product_dict["created_at"]=datetime.utcnow().isoformat()+'Z'
    try:
        add_products(product_dict)
    except ValueError as e:
        raise HTTPException(status_code=400,detail="Error in the updation of the data")
    return product

@app.delete("/products/{product_id}")
def remove_product(product_id : UUID = Path(...,description="product-uuid")):
    try:
        data=delete_product(str(product_id))
    except ValueError as e:
        raise HTTPException(status_code=400,detail="Error in the deletion of the data")
    return data