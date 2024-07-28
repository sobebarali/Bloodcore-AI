from fastapi import UploadFile, HTTPException
from .utils import extract_text_from_pdf, save_pdf_file
from ..auth.schemas import User
from bloodcore.crew import BloodcoreCrew


async def create_blood_test_report(email: str, pdf_file: UploadFile, current_user: User):
    pdf_path = await save_pdf_file(pdf_file)
    
    # Extract text from the PDF
    try:
        blood_test_report_text = extract_text_from_pdf(pdf_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error extracting text from PDF: {e}")

    # Run the BloodcoreCrew to process the PDF file
    inputs = {'blood_test_report': blood_test_report_text}
    
    try:
        # Run your crew process here
        # report = BloodcoreCrew().crew().kickoff(inputs=inputs)
        
        # Process the text with the CrewAI setup
        result = BloodcoreCrew().crew().kickoff(inputs=inputs)
       
        return {"email": email, "pdf_url": pdf_path, "extracted_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the report: {e}")
