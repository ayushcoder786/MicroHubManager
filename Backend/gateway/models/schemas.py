from pydantic import BaseModel

class SigninSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str

class SignupSchema(BaseModel):
    email: str
    password: str