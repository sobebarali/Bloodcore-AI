from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from .service import create_blood_test_report
from ..auth.service import get_user
from ..auth.schemas import User

router = APIRouter()

@router.post("/upload")
async def upload_blood_test_report(
    email: str = Form(...),
    pdf_file: UploadFile = File(...),
    current_user: User = Depends(get_user),
):
      
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    

    if pdf_file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid PDF file")
    
    try:
        report = await create_blood_test_report(email, pdf_file, current_user)
        return {"message": "Blood test report uploaded successfully", "report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))