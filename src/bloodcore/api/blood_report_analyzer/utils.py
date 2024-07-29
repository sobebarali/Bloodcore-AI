import os
from fastapi import UploadFile
import fitz

async def save_pdf_file(pdf_file: UploadFile):
    # Generate a unique filename for the PDF file
    filename = f"{pdf_file.filename}"
    
    # Specify the directory to save the PDF file
    save_dir = "uploads/"
    
    # Create the directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    
    # Save the PDF file to the specified directory
    file_path = os.path.join(save_dir, filename)
    with open(file_path, "wb") as file:
        file.write(await pdf_file.read())
    
    # Return the URL or path of the saved PDF file
    return file_path

def extract_text_from_pdf(pdf_file_path):
    """Extract text from a PDF file."""
    document = fitz.open(pdf_file_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text