from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
#Security module
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

#Instance of oauth2 to handle authentication
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    #Use types  for all attributes
    username:str
    full_name: str
    email:str
    disabled: bool

class UserDB(User):
    #User in the database, it is the same but it has a password
    password :str

users_db = {
    "mouredev":{
         "username" : "mouredev",
         "full_name" : "Brais Moure ",
         "email" : "test@test.com",
         "disabled": False,
         "password": "123456"
     },
    "mouredev2":{
         "username" : "mouredev2",
         "full_name" : "Brais Moure  2 ",
         "email" : "test2@test.com",
         "disabled": True,
         "password": "12345"
     }

 }   

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])   

#Function to validate token, depends on oauth2 object that will generate token 
async def current_user(token:str = Depends(oauth2)):
    #Since our token is username, search if an user exists for that username
    user = search_user_db(token)
    if not user: 
      raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Credenciales autenticacion invalidas",headers={"WWW-Authenticate":"Bearer"})  
    if user.disabled:
        raise  HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Usuario Inactivo")  
    return search_user(token)

    

@app.post("/login")
async def login(form:OAuth2PasswordRequestForm = Depends()):   
    user_db = users_db.get(form.username)

    if not user_db:
        raise  HTTPException(status_code=400,detail="Usuario no es correcto")
    
    user = search_user_db(form.username)

    if not form.password == user.password:
        raise  HTTPException(status_code=400,detail="Contraseña incorrecta")
    
    #User is authenticated
    return {"access_token": user.username,"token_type": "bearer"}

@app.get("/users/me")
#Dependency criteria is defined by function current_user which return an User
async def me(user:User = Depends(current_user)):
    return user
