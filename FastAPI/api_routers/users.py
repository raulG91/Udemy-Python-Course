
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel

#app = FastAPI()

router = APIRouter(tags=["Users"])

class User(BaseModel):
    #Use types  for all attributes
    id:int
    name:str
    surname:str
    url :str
    edad:int 


users_list = [User(id=1,name="Raul",surname="Garcia",url="http://test.com",edad=35),User(id=2,name="Juan",surname="Garcia",url="http://juan.com",edad=20),User(id=3,name="Maria",surname="Garcia",url="http://maria.com",edad=31)]

@router.get('/users')
async def users():
    return users_list

@router.get("/user/{id}") #Path
async def user(id:int):
    #Use python function filter to get element from the list
    user =  filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return{"error": "No se ha encontrado el usuario" }
    
@router.get("/userquery/")
async def user(id:int): #Query 
    #Use python function filter to get element from the list
    user =  filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return{"error": "No se ha encontrado el usuario" }
    
@router.post("/user/",status_code=201) #Post
async def new_user(user:User):
    users_list.append(user)

@router.put("/user/") 
async def update_user(user:User):
    encontrado = False
    for index,saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            encontrado = True
    if encontrado:
        return user
    else:
       raise HTTPException(404,detail="No encontrado")
    
       

@router.delete("/user/{id}")
async def delete_user(id:int):
    encontrado = False
    for index,saved_user in enumerate(users_list):
        if saved_user.id == id:
           del(users_list[index])
           encontrado = True
    if encontrado:
        return {"Se ha eliminado el usuario"}
    else:
        return {"error": "No encontrado" } 