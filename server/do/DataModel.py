from pydantic import BaseModel
from typing import List

class DataModel(BaseModel):
    data: List[str] = []


class PricePredictionModel(BaseModel):
    mileage : int
    year : int
    make : str
    model : str
    fuel : str
    gear : str
    offerType : str