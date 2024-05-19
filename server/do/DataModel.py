from pydantic import BaseModel
from typing import List

class DataModel(BaseModel):
    data: List[str] = []