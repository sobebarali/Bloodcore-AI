from pydantic import BaseModel, EmailStr

class BloodTestReport(BaseModel):
    email: EmailStr
    pdf_url: str