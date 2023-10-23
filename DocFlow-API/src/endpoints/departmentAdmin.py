from fastapi import APIRouter
from fastapi import Query
from fastapi.responses import FileResponse
from src.models.departmentAdmin import DepartmentAdmin,DepartmentAdminController


router = APIRouter(
    prefix="/departmentAdmin",
    tags=["departmentAdmin"],
    responses={404: {"description": "Not found","Access-Control-Allow-Origin": "http://localhost:8081"}},
)

@router.get("/{id}")
async def get_data(id:int):
    db_control=DepartmentAdminController()
    result=db_control.get_data(id)
    return result

@router.post("/add/")
async def add(departmentAdmin:DepartmentAdmin):
    db_control=DepartmentAdminController()
    result=db_control.add(document.dict())
    return result

@router.post("/update/{id}")
async def update(departmentAdmin:DepartmentAdmin,id:int):
    db_control=DepartmentAdminController()
    result=db_control.update(departmentAdmin.dict(),id)
    return result

@router.get("/delete/{id}")
async def delete(id:int):
    db_control=DepartmentAdminController()
    result=db_control.delete(id)
    return result
