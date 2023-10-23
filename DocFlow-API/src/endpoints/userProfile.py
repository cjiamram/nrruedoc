from fastapi import APIRouter, UploadFile
from fastapi import Query
from fastapi.responses import FileResponse
from src.models.userProfile import UserProfileBase,UserProfile,UserProfileController
import os

router = APIRouter(
    prefix="/userprofile",
    tags=["userprofile"],
    responses={404: {"description": "Not found","Access-Control-Allow-Origin": "http://localhost:8081"}},
)

UPLOAD_FOLDER = "pictures"  # Change this to your desired folder path


@router.get("/get_picture/{image_name}")
async def get_picture(image_name: str):
    try:
        image_path = os.path.join(UPLOAD_FOLDER,image_name)
        if os.path.exists(image_path):
            file_obj=FileResponse(image_path, media_type="image/jpeg")
        else:
            image_path = os.path.join(UPLOAD_FOLDER, "user.jpg")

            file_obj=FileResponse(image_path, media_type="image/jpeg")
        return file_obj
    except Exception as e:

        return {"error": str(e)}



@router.post("/upload_and_rename/{new_file_name}")
async def upload_and_rename_file(file: UploadFile,new_file_name):
    try:
        # Create the folder if it doesn't exist
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        # Generate a new file name (e.g., using a timestamp or a unique ID)
        #new_file_name =new_filename  # Change this to your desired new file name
        # Combine the folder path with the new file name to create the full file path
        file_path = os.path.join(UPLOAD_FOLDER, new_file_name)
        # Save the uploaded file to a temporary location
        with open(file_path, "wb") as temp_file:
            temp_file.write(file.file.read())
        return {"message": "File uploaded and renamed successfully","file_path": file_path,"file_name":new_file_name,"is_exist":True,}
    except Exception as e:
        return {"error": str(e)}


@router.post("/add/")
async def add(userProfile:UserProfile):
    db_control=UserProfileController()
    result=db_control.add(userProfile.dict())
    return result


@router.put("/update/{id}")
async def update(userProfile:UserProfile,id:int):
    db_control=UserProfileController()
    result=db_control.update(userProfile.dict(),id)
    return result

@router.get("/delete/{id}")
async def delete(id:int):
    db_control=UserProfileController()
    result=db_control.delete(id)
    return result


@router.get("/get_data/{id}")
async def get_data(id:int):
    db_control=UserProfileController()
    result=db_control.get_data(id)
    return result


@router.get("/get_data_by_user_code/{user_code}")
async def get_data_by_user_code(user_code:str):
    db_control=UserProfileController()
    result=db_control.get_data_by_user_code(user_code)
    return result
