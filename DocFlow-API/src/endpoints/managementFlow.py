from fastapi import APIRouter, UploadFile
from fastapi import Query
from fastapi.responses import FileResponse
from src.models.managementFlow import ManagementFlowBase,ManagementFlow,ManagementFlowController
import os

router = APIRouter(
    prefix="/managementFlow",
    tags=["managementFlow"],
    responses={404: {"description": "Not found","Access-Control-Allow-Origin": "http://localhost:8081"}},
)

@router.get("/{id}")
async def get_data(id:int):
    db_control=ManagementFlowController()
    result=db_control.get_data(id)
    return result


@router.post("/add/")
async def add_managementFlow(managementFlow:ManagementFlowBase):
    db_control=CustomerController()
    result=db_control.add(managementFlow.dict())
    return result


@router.post("/update/{id}")
async def add_customer(managementFlow:ManagementFlowBase,id:int):
    db_control=CustomerController()
    result=db_control.update(managementFlow.dict(),id)
    return result


@router.get("/delete/{id}")
async def delete(id:int):
    db_control=ManagementFlowController()
    result=db_control.delete(id)
    return result


@router.get("/read_data/{id}")
async def read_data(id:int):
    db_control=ManagementFlowController()
    result=db_control.read_data(id)
    return result
