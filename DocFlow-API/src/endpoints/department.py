from fastapi import APIRouter, UploadFile
from fastapi import Query
from fastapi.responses import FileResponse
from src.models.department import Department,DepartmentController

router = APIRouter(
    prefix="/department",
    tags=["department"],
    responses={404: {"description": "Not found","Access-Control-Allow-Origin": "http://localhost:8081"}},
)


@router.get("/get_head_department/")
async def get_head_department():
    db_control=DepartmentController()
    results=db_control.get_head_department()
    return results


@router.get("/get_child_department/{head}")
async def get_child_department(head:str):
    db_control=DepartmentController()
    results=db_control.get_child_department(head)
    return results


@router.get("/get_level_department/")
async def get_level_department():
    db_control=DepartmentController()
    results=db_control.get_level_department()
    results_dep=[]
    head=""
    head_index=0
    child_index=1
    for r in results:
        if r['parent']==True:
            dep={"id":r['id'],"department_code":r['department_code'],"department_name":str(head_index+1)+" "+r['department_name']}
            head=r['department_name']
            child_index=1
            head_index+=1
        else:
            dep={"id":r['id'],"department_code":r['department_code'],"department_name":"-"+str(head_index)+"."+str(child_index)+" "+head+'->'+r['department_name']}
            child_index+=1

        results_dep.append(dep)

    return results_dep;

@router.get("/get_prefix/{department_code}")
async def get_prefix(department_code:str):
    db_control=DepartmentController()
    result=db_control.get_prefix(department_code)
    return result
