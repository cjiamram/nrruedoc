from fastapi import APIRouter
from fastapi import Query
from src.models.documentType import DocumentType


router = APIRouter(
    prefix="/documentType",
    tags=["documentType"],
    responses={404: {"description": "Not found","Access-Control-Allow-Origin": "http://localhost:8081"}},
)

@router.get("/get_decument_type/")
async def get_decument_type():
    db_control=DocumentType()
    results=db_control.get_decument_type()
    return results
