from pydantic import BaseModel
from typing import Optional
class User(BaseModel):
    #Use types  for all attributes
    #Id could be optional idicate it, because it will be generated by db
    id: Optional[str] = None
    username:str
    email:str