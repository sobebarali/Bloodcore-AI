from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class User(BaseModel):
    id: str
    email: str
    disabled: bool = False