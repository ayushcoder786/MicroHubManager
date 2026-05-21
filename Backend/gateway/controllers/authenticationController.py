from fastapi import APIRouter , Header
from models.schemas import SigninSchema, SignupSchema
import httpx
router = APIRouter(prefix="/authservice")

SPRING_URL = "http://localhost:8081/"

@router.post("/signup")
async def signup(U: SignupSchema):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SPRING_URL + "user/signup",
            json=U.model_dump() )
    return response.json()

@router.post("/signin")
async def signin(U: SigninSchema):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SPRING_URL + "user/signin",
            json=U.model_dump() )
    return response.json()

@router.get("/uinfo")
async def uinfo(Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            SPRING_URL + "user/uinfo",
            headers={"Token": Token}
        )
    return response.json()

@router.get("/profile")
async def profile(Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            SPRING_URL + "user/profile",
            headers={"Token": Token}
        )
    return response.json()

@router.get("/getallusers/{PAGE}/{SIZE}")
async def profile(PAGE: int, SIZE: int, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{SPRING_URL}user/getallusers/{PAGE}/{SIZE}",
            headers = {"Token": Token}
        )
    return response.json()