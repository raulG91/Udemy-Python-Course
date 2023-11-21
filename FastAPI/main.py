from fastapi import FastAPI
from api_routers import products,users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)
app.mount("/static",StaticFiles(directory="static"),name="static")


@app.get("/")
def read_root():
    return {"Hello": "World"}

