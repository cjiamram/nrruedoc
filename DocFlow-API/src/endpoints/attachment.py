from fastapi import APIRouter, UploadFile
from fastapi import Query
from fastapi.responses import FileResponse
from src.models.attachment import Attachment,AttachmentBase,AttachmentController
from typing import List
from pathlib import Path
import shutil
import fitz  # PyMuPDF
import os


router = APIRouter(
    prefix="/attachment",
    tags=["attachment"],
    responses={404: {"description": "Not found","Access-Control-Allow-Origin": "http://localhost:8081"}},
)

UPLOAD_FOLDER = "uploads"  # Change this to your desired folder path

def extract_text_from_pdf(file_path: str) -> List[str]:
    text_content = []
    try:
        with fitz.open(file_path) as pdf_document:
            for page_number in range(pdf_document.page_count):
                page = pdf_document[page_number]
                text_content.append(page.get_text())
    except Exception as e:
        return [f"Error reading PDF: {str(e)}"]
    return text_content


@router.get("/read_documents/{id}")
async def read_pdf_to_text(id:int):
    db_control=AttachmentController()
    file_path=UPLOAD_FOLDER+"/"+db_control.get_file_name_by_id(id)
    return extract_text_from_pdf(file_path)


@router.get("/read_pdf/{id}")
async def read_pdf(id:int):
    # Check if the file exists
    db_control=AttachmentController()
    file_path=Path(UPLOAD_FOLDER+"/"+db_control.get_file_name_by_id(id))
    if not file_path.is_file():
        return {"error": "PDF file not found"}

    # Return the PDF file as response
    return FileResponse(file_path, media_type='application/pdf')



@router.post("/add/")
async def add(attachment:Attachment):
    db_control=AttachmentController()
    result=db_control.add(attachment.dict())
    return result


@router.put("/update/{id}")
async def update(attachment:Attachment,id:int):
    db_control=CustomerController()
    result=db_control.update(document.dict(),id)
    return result

@router.get("/delete/{id}")
async def delete(id:int):
    db_control=AttachmentController()
    file=db_control.get_file_name_by_id(id)
    result=db_control.delete(id)

    file_path=UPLOAD_FOLDER+"/"+file
    try:
        # Delete the file
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except OSError as e:
        print(f"Error: {file_path} : {e.strerror}")
    return result

@router.get("/delete_by_document_id/{document_id}")
async def delete_by_document_id(document_id:str):
    db_control=AttachmentController()
    result=db_control.delete_by_document_id(document_id)
    path=UPLOAD_FOLDER+"/"+document_id
    try:
        # Delete the folder and its contents
        shutil.rmtree(path)
        print(f"Folder '{path}' and its contents deleted successfully.")
    except OSError as e:
        print(f"Error: {path} : {e.strerror}")
    return result

@router.get("/get_attachments/{document_id}")
async def get_attachments(document_id:str):
    db_control=AttachmentController()
    results=db_control.get_attachments(document_id)
    return results
