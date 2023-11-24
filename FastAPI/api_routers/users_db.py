
from fastapi import FastAPI, HTTPException, APIRouter, status
from pydantic import BaseModel
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

#app = FastAPI()

router = APIRouter(tags=["UsersDB"])



users_list = []

@router.get('/usersdb/',response_model=list[User])
async def users():
    #return users_list
    return users_schema(db_client.local.users.find())

@router.get("/userdb/{id}") #Path
async def user(id:str):
    #Create ObjectId which is the representation in MongoDB for id
    return search_user("_id",ObjectId(id))
'''    
@router.get("/userquerydb/")
async def user(id:int): #Query 
    #Use python function filter to get element from the list
    user =  filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return{"error": "No se ha encontrado el usuario" }
'''    
@router.post("/userdb/",status_code=201) #Post
async def new_user(user:User):
    #First check if the user already exist

   if type(search_user("email",user.email)) == User:
        raise  HTTPException(status_code=404,detail="Usuario ya existe")
   #Mongo DB will work with JSON object, therefore we transform into a dict
   user_dict = dict(user)
   del user_dict['id'] # Database will generate it
   #Use local database
   id = db_client.local.users.insert_one(user_dict).inserted_id

    #Get the user created, _id is the id created by Mongo DB and transform the result to json
   new_user = user_schema(db_client.local.users.find_one({"_id":id}))
    #Create user from JSON, it is possible because inherit BaseModel
   return User(**new_user)
@router.put("/userdb/") 
async def update_user(user:User):
    #Transform user into a dictionay and delete field id. Id is maintained in DB and should not be updated
    user_dict = dict(user)
    del(user_dict['id'])

    try:
        db_client.local.users.find_one_and_replace({"_id":ObjectId(user.id)},user_dict)
    except:  
        raise HTTPException(404,detail="No encontrado")  
    return search_user("_id",ObjectId(user.id))
@router.delete("/userdb/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id:str):
   #Find and delete, it will return deleted object
   found = db_client.local.users.find_one_and_delete({"_id":ObjectId(id)})

   if not found:
       return {"error":"No se ha eliminado el usuario" }

'''    
def search_user_by_email(email:str):

    try:
       new_user = user_schema(db_client.local.users.find_one({"email": email}))
       return User(**new_user)
    except:
        return {"error": "No encontrado" }   
'''
def search_user(field:str, key):
    '''
    Search user in the data with a given criteria
    '''
    try:
       new_user = user_schema(db_client.local.users.find_one({field: key}))
       return User(**new_user)
    except:
        return {"error": "No encontrado" }   
