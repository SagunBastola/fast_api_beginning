from os import path
from typing import List,Dict
import json
from pathlib import Path

data_file = Path(__file__).parent.parent / "data" / "products.json"

def load_products() -> List[Dict]:
    if not data_file.exists():
        return []
    with open(data_file,"r",encoding="utf-8") as file:
        return json.load(file)

def get_all_products() -> List[Dict]:
    return load_products()