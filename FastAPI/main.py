from fastapi import FastAPI
from api_routers import products,users,jwt_auth_users,basic_auth_users,users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth_users.router)
app.include_router(basic_auth_users.router)
app.include_router(users_db.router)
app.mount("/static",StaticFiles(directory="static"),name="static")


@app.get("/")
def read_root():
    return {"Hello": "World"}

# Ini server uvicorn main:app --reload 
# Generate documentation http://127.0.0.1:8000/docs