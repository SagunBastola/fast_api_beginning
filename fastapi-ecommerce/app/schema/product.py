

from typing import List,Dict, Literal,Optional
from pydantic import BaseModel, EmailStr,Field,AnyUrl, field_validator, model_validator, computed_field
from uuid import UUID
from datetime import datetime

class Dimension(BaseModel):
    length : float = Field(..., ge=0)
    width : float =Field(...,ge=0)
    height : float = Field(...,ge=0)

class Seller(BaseModel):
    seller_id : UUID
    name : str
    email : EmailStr
    website : AnyUrl

class Product(BaseModel):
    id : UUID
    sku : str = Field(...,description="SKU",examples=["XIAO-359GB-001"])
    name : str
    description : str = Field(...,description="describe about the product")
    category : str =Field(..., examples=["laptop","electronics"],description="category of the product")
    brand : str
    price : float = Field(...,ge=0)
    currency :Literal["INR"]
    discount_percent :float = Field(...,ge=0,le=100)
    stock:int
    is_active: bool
    rating : float =Field(...,ge=0,le=5)
    tags : Optional[List[str]]
    image_urls : List[AnyUrl]
    dimensions_cm : Dimension 
    seller: Seller 
    created_at : datetime

    @field_validator("sku", mode="after")
    @classmethod
    def validate_sku(cls, v: str):
        if "-" not in v:
            raise ValueError("- must be present in the sku")

        if len(v) < 4 or v[-4] != "-":
            raise ValueError("error 2")

        if not v[-3:].isdigit():
            raise ValueError("error 3")

        return v
    
    @model_validator(mode="after")
    @classmethod
    def skock_is_active_validation(cls,values : "Product"):
        if values.stock==0:
            if not values.is_active:
                return values
            else:
                ValueError("when stock is 0 must be false")
        else:
            if values.is_active:
                return values
            else:
                ValueError("is active must be true")
    
    @computed_field
    @property
    def discounted_price(self) -> float:
        return (100-self.discount_percent)*self.price/100
    
    @computed_field
    @property
    def volume(self) -> float:
        return self.dimensions_cm.length*self.dimensions_cm.height*self.dimensions_cm.width
Product.model_rebuild()        
    
