
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel


#app = FastAPI()

router = APIRouter(prefix="/products",tags=["Product"],responses={404: {"message":"No encontrado"}})

products_list = ["Producto 1","Product 2", "Product 3"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}/")
async def product(id:int):
    return products_list[id]