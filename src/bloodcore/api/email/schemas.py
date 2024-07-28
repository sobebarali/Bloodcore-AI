from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    email: EmailStr
    subject: str
    body: str