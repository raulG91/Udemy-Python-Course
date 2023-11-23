
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema

#app = FastAPI()

router = APIRouter(tags=["UsersDB"])



users_list = []

@router.get('/usersdb/')
async def users():
    return users_list

@router.get("/userdb/{id}") #Path
async def user(id:int):
    #Use python function filter to get element from the list
    user =  filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return{"error": "No se ha encontrado el usuario" }
    
@router.get("/userquerydb/")
async def user(id:int): #Query 
    #Use python function filter to get element from the list
    user =  filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return{"error": "No se ha encontrado el usuario" }
    
@router.post("/userdb/",status_code=201) #Post
async def new_user(user:User):
   # users_list.append(user)
   user_dict = dict(user)
   del user_dict['id'] # Database will generate it
   #Use local database
   id = db_client.local.users.insert_one(user_dict).inserted_id
   print(id)
    #Get the user created, _id is the id created by Mongo DB and transform the result to json
   new_user = user_schema(db_client.local.users.find_one({"_id":id}))
    #Create user from JSON, it is possible because inherit BaseModel
   return User(**new_user)
@router.put("/userdb/") 
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
    
       

@router.delete("/userdb/{id}")
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