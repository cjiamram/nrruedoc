from fastapi import APIRouter, UploadFile
from fastapi import Query
from fastapi.responses import FileResponse
from src.models.signature import Signature,SignatureBase,SignatureController
import os

router = APIRouter(
    prefix="/signature",
    tags=["signature"],
    responses={404: {"description": "Not found"}},
)

UPLOAD_FOLDER="ca"


@router.post("/add/")
async def add(signature:Signature):
    db_control=SignatureController()
    result=db_control.add(signature.dict())
    return result


@router.put("/update/{id}")
async def update(signature:Signature,id:int):
    db_control=SignatureController()
    result=db_control.update(signature.dict(),id)
    return result

@router.get("/delete/{id}")
async def delete(id:int):
    db_control=SignatureController()
    result=db_control.delete(id)
    return result


@router.get("/get_data/{id}")
async def get_data(id:int):
    db_control=SignatureController()
    result=db_control.get_data(id)
    return result


@router.get("/get_data_by_user_code/{user_code}")
async def get_data_by_user_code(user_code:str):
    db_control=SignatureController()
    result=db_control.get_data_by_user_code(user_code)
    return result


@router.get("/get_picture/{user_code}/{image_name}")
async def get_picture(user_code:str,image_name: str):
    try:
        #image_path=UPLOAD_FOLDER
        image_path = os.path.join(UPLOAD_FOLDER,user_code)
        image_path=os.path.join(image_path, image_name)
        if os.path.exists(image_path):
            #file_obj=FileResponse(image_path, media_type="image/jpeg")
            file_obj=FileResponse(image_path, media_type="image/jpeg")
        else:
            image_path = os.path.join(UPLOAD_FOLDER, "Stamp.jpg")

            file_obj=FileResponse(image_path, media_type="image/jpeg")
        return file_obj
    except Exception as e:

        return {"error": str(e)}


@router.post("/put_stamp/{user_code}/{stamp_type}")
async def put_stamp(file: UploadFile,user_code:str,stamp_type:int):
    Flag=False
    file_name=file.filename
    try:
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        new_path=UPLOAD_FOLDER+"/"+user_code
        os.makedirs(new_path, exist_ok=True)
        file_path = os.path.join(new_path, file_name)
        # Write the file to the specified location
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        Flag=True
    except Exception as e:
        Flag=False


    db_control=SignatureController()
    result=db_control.put_stamp(file_name,user_code,stamp_type)
    result["Flag_upload"]=Flag
    return result



@router.post("/upload_ca/{user_code}/")
async def upload_ca(user_code,file: UploadFile):
    try:
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        #directory_path = UPLOAD_FOLDER
        #os.chdir(directory_path)
        new_path=UPLOAD_FOLDER+"/"+user_code
        os.makedirs(new_path, exist_ok=True)

        file_path = os.path.join(new_path, file.filename)

        # Write the file to the specified location
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        return {"filename": file.filename, "path": file_path}
    except Exception as e:
        return {"error": str(e)}


# @router.get("/get_picture/{image_name}")
# async def get_picture(image_name: str):
#     try:
#         image_path = os.path.join(UPLOAD_FOLDER, image_name)
#         #image_path = os.path.join(UPLOAD_FOLDER, "User.jpg")
#         if os.path.exists(image_path):
#             file_obj=FileResponse(image_path, media_type="image/jpeg")
#         else:
#             image_path = os.path.join(UPLOAD_FOLDER, "Stamp.jpg")
#             file_obj=FileResponse(image_path, media_type="image/jpeg")
#         return file_obj
#     except Exception as e:
#
#         return {"error": str(e)}
