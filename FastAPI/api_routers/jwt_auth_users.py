from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from pydantic import BaseModel
#Security module
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt,JWTError
from passlib.context import CryptContext
from datetime import timedelta,datetime

#Algoritmo de encriptacion token jwt
ALGORITHM = "HS256"
#Token duration
TOKEN_DURATION = 5
#Secret key
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

router = APIRouter(prefix="/users_jwt",tags=["Users JWT"],responses={404: {"message":"No encontrado"}})

#Algorthm used for password encryption
crypt = CryptContext(schemes=["bcrypt"])

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
         #"password": "123456"
         "password" : "$2a$10$uA5NRTooPfWt/JDqjOTRROxaQV6XGcQNGgbXFRYMQZiPKFkqCUFrm"
     },
    "mouredev2":{
         "username" : "mouredev2",
         "full_name" : "Brais Moure  2 ",
         "email" : "test2@test.com",
         "disabled": True,
         "password": "$2a$10$F5vHwFkv66xrTEqyfTL5P.UDBGmExJAi.WSKVo08jKhkPrOoWdSzi"
     }

 }   
def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])   


@router.post("/login")
async def login(form:OAuth2PasswordRequestForm = Depends()):   
    user_db = users_db.get(form.username)

    if not user_db:
        raise  HTTPException(status_code=400,detail="Usuario no es correcto")
    
    user = search_user_db(form.username)

    crypt.verify(form.password, user.password)
    
    if not crypt.verify(form.password, user.password):
        raise  HTTPException(status_code=400,detail="Contraseña incorrecta")
    
    # Set token duration    
    expire_time = datetime.utcnow() + timedelta(minutes=TOKEN_DURATION)
    access_token = {
        #Fields normally defined in jwt
        "sub": user.username,
        "exp": expire_time,
        
        
    }
    #User is authenticated
    return {"access_token": jwt.encode(access_token,SECRET_KEY,algorithm=ALGORITHM),"token_type": "bearer"}

async def auth_user(token:str = Depends(oauth2)):
    #Decrypt token to get username
    try:
        username = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Credenciales autenticacion invalidas",headers={"WWW-Authenticate":"Bearer"}) 
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Credenciales autenticacion invalidas",headers={"WWW-Authenticate":"Bearer"})  
  
    user = search_user(username)
    if not user: 
      raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Credenciales autenticacion invalidas",headers={"WWW-Authenticate":"Bearer"})  
    return user

#Function to validate token, depends on oauth2 object that will generate token 
async def current_user(user:User = Depends(auth_user)):

    if user.disabled:
        raise  HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Usuario Inactivo")  
    return user

@router.get("/users/me")
#Dependency criteria is defined by function current_user which return an User
async def me(user:User = Depends(current_user)):
    return user
