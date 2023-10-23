from fastapi import APIRouter, UploadFile
from fastapi import Query
from fastapi.responses import FileResponse
from src.models.document import Document,DocumentBase,DocumentController
import os

router = APIRouter(
    prefix="/document",
    tags=["document"],
    responses={404: {"description": "Not found"}},
)

UPLOAD_FOLDER = "uploads"  # Change this to your desired folder path


@router.get("/{id}")
async def get_data(id:int):
    db_control=DocumentController()
    result=db_control.get_data(id)
    return result


@router.post("/add/")
async def add(document:DocumentBase):
    db_control=DocumentController()
    result=db_control.add(document.dict())
    return result


@router.put("/update/{id}")
async def update(document:DocumentBase,id:int):
    db_control=DocumentController()
    result=db_control.update(document.dict(),id)
    return result



@router.get("/get_doc_no_by_id/{id}")
async def get_doc_no_by_id(id:int):
    db_control=DocumentController()
    result=db_control.get_doc_no_by_id(id)
    return result

@router.get("/read_data/{id}")
async def read_data(id:int):
    db_control=DocumentController()
    result=db_control.read_data(id)
    return result

@router.get("/delete/{id}")
async def delete(id:int):
    db_control=DocumentController()
    result=db_control.delete(id)
    return result

@router.get("/get_max_id/")
async def get_max_id():
    db_control=DocumentController()
    result=db_control.get_max_id()
    return result

@router.get("/update_status/{status}/{id}")
async def update_status(status,id:int):
    db_control=DocumentController()
    result=db_control.update_status(status,id)
    return result


@router.get("/update_stage/{stage}/{id}")
async def update_stage(status,id:int):
    db_control=DocumentController()
    result=db_control.update_stage(stage,id)
    return result

@router.get("/search_doc_by_owner/{user_code}/{status}")
async def search_doc_by_owner(user_code,status):
    db_control=DocumentController()
    results=db_control.search_doc_by_owner(user_code,status)
    return results

@router.get("/get_doc_no/{department_code}/")
async def get_doc_no(department_code):
    db_control=DocumentController()
    result=db_control.get_doc_no(department_code)
    return result


@router.post("/upload_doc/{doc_no}/")
async def upload_doc(doc_no,file: UploadFile):
    try:
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        #directory_path = UPLOAD_FOLDER
        #os.chdir(directory_path)
        new_path=UPLOAD_FOLDER+"/"+doc_no
        os.makedirs(new_path, exist_ok=True)

        file_path = os.path.join(new_path, file.filename)

        # Write the file to the specified location
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        return {"filename": file.filename, "path": file_path}
    except Exception as e:
        return {"error": str(e)}
