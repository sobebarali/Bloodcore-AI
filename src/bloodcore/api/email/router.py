from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from bloodcore.api.auth.router import get_current_user
from .schemas import EmailRequest
from .service import send_email

from ..auth.schemas import User

router = APIRouter()

@router.post("/send")
async def send_analysis_email(
    email_request: EmailRequest,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
):
    try:
        background_tasks.add_task(
            send_email,
            email_request.email,
            email_request.subject,
            email_request.body,
            current_user,
        )
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))