from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] #como el id sera autogenerado es opcional que sea proporcionado 
    name: str
    email: str
    password: str
