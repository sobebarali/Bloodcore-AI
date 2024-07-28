from pydantic import BaseModel, EmailStr
from typing import Optional

class EmailRequest(BaseModel):
    email: EmailStr
    subject: str
    body: str
    attachment: Optional[str] = None  # Base64-encoded file content
