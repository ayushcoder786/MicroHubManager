# from fastapi import APIRouter
# from models.schemas import SigninSchema, SignupSchema
# import httpx

# router = APIRouter(prefix="/authservice")



# @router.post("/signup")
# async def signup(U: SignupSchema):
#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             SPRING_URL + "user/signup",
#             json=U.model_dump()   # Send data to Spring
#         )
#     return response.json() # Returs back the response received from spring

# @router.post("/signin")
# async def signin(U: SigninSchema):
#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             SPRING_URL + "user/signin",
#             json=U.model_dump()
#         )
#     return response.json()

from fastapi import APIRouter
from models.schemas import SigninSchema, SignupSchema

router = APIRouter(prefix="/authservice")

@router.post("/signup")
async def signup(U: SignupSchema):
    return {
        "code":200, 
        "message" : U
    }

@router.post("/signin")
async def signin(U: SigninSchema):
    return {
        "code":200,
        "message": U
    }
