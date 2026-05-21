
from pydantic import BaseModel

class SigninSchema(BaseModel):
    username:str
    password:str

class SignupSchema(BaseModel):
    fullname:str
    phone:str
    email:str
    password:str
    retypepassword:str