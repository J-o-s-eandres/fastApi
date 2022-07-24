from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    # como el id sera autogenerado es opcional que sea proporcionado
    id: Optional[str]
    name: str
    email: str
    password: str
