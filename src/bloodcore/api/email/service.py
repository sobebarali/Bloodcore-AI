from .utils import send_email_async
from ..auth.schemas import User

async def send_email(email: str, subject: str, body: str, current_user: User):
    await send_email_async(email, subject, body)
    