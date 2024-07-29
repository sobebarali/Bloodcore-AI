from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, UploadFile, File, Form
from bloodcore.api.auth.router import get_current_user
from .service import send_email_async
from ..auth.schemas import User
from typing import Optional

router = APIRouter()

@router.post("/send")
async def send_analysis_email(
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    email: str = Form(...),
    subject: str = Form(...),
    body: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        attachment = None
        if file:
            attachment = await file.read()

        background_tasks.add_task(
            send_email_async,
            email,
            subject,
            body,
            attachment,  # Pass attachment data
        )
        return {"message": "Email is being sent in the background"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
