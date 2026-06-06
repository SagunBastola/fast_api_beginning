from math import prod
from os import path
from typing import List,Dict
import json
from pathlib import Path

data_file = Path(__file__).parent.parent / "data" / "dummy.json"

def load_products() -> List[Dict]:
    if not data_file.exists():
        return []
    with open(data_file,"r",encoding="utf-8") as file:
        return json.load(file)

def get_all_products() -> List[Dict]:
    return load_products()

def save_products(products : List[Dict]) -> None:
    with open(data_file,"w",encoding="utf-8") as file:
        json.dump(products,file,indent=2,ensure_ascii=False)

def add_products(product : Dict) -> Dict :
    products=get_all_products()
    
    if any(p["sku"] == product["sku"] for p in products):
        raise ValueError("sku already exists")
    products.append(product)
    save_products(products)
    return product

def delete_product(id : str):
    products=get_all_products()
    
    for idx,p in enumerate(products):
        if p["id"] == id :
            deleted=products.pop(idx)
            save_products(products)
            return {"deleted" : deleted}
    return {"failed in deletion"}
    
def change_product(product_id: str, update_data: Dict):
    products = get_all_products()

    for index, product in enumerate(products):
        if product["id"] == product_id:

            for key, value in update_data.items():

                if value is None:
                    continue

                if (
                    isinstance(value, dict)
                    and isinstance(product.get(key), dict)
                ):
                    product[key].update(value)
                else:
                    product[key] = value

            products[index] = product
            save_products(products)
            return product

    raise ValueError("Product not found!")