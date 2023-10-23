from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from src.util.dbcontroller import DBController as DB

class DepartmentAdminBase(BaseModel):
    user_code:str
    department_code:str
    description:str


class DepartmentAdmin(DepartmentAdminBase):
    created_at:datetime=None
    updated_at:datetime=None

class DepartmentAdminController():
    __tablename__="department_admin"

    def add(self,departmentAdmin):
        db=DB(self.__tablename__)
        departmentAdmin["created_at"]=datetime.today()
        del departmentAdmin["updated_at"]
        result=db.create()
        del db
        return result

    def update(self,departmentAdmin,id):
        db=DB(self.__tablename__)
        today=datetime.today()
        del departmentAdmin['created_at']
        departmentAdmin["updated_at"]=today
        result=db.update(departmentAdmin,id)
        del db
        return result

    def delete(self,id):
        db=DB(self.__tablename__)
        result=db.delete(id)
        del db
        return result

    def get_data(self,id):
        db=DB(self.__tablename__)
        fields=["id","user_code","department_code","description"]
        result=db.get_data(fields,id)
        return result
