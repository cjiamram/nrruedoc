from fastapi import APIRouter
from fastapi import Query
from fastapi.responses import FileResponse
from src.models.templateFlow import TemplateFlow,TemplateFlowController

router = APIRouter(
    prefix="/templateFlow",
    tags=["templateFlow"],
    responses={404: {"description": "Not found","Access-Control-Allow-Origin": "http://localhost:8081"}},
)

@router.post("/add/")
async def add(templateFlow:TemplateFlow):
    db_control=TemplateFlowController()
    result=db_control.add(templateFlow.dict())
    return result


@router.put("/update/{id}")
async def update(templateFlow:TemplateFlow,id:int):
    db_control=TemplateFlowController()
    result=db_control.update(templateFlow.dict(),id)
    return result


@router.get("/delete/{id}")
async def delete(id:int):
    db_control=TemplateFlowController()
    result=db_control.delete(id)
    return result


@router.get("/get_data/{id}")
async def get_data(id:int):
    db_control=TemplateFlowController()
    result=db_control.get_data(id)
    return result


@router.get("/search_data/{keyword}")
async def search_data(keyword:str):
    db_control=TemplateFlowController()
    results=db_control.search_data(keyword)
    return results
