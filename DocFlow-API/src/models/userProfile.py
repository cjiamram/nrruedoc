from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from src.util.dbcontroller import DBController as DB



class UserProfileBase(BaseModel):
    user_code:str
    user_name_th:str
    user_name_en:str
    department_code:str
    picture:str
    description:str
    email:str

class UserProfile(UserProfileBase):
    created_at:datetime=None
    updated_at:datetime=None


class UserProfileController():
    __tablename__="user_profiles"


    def add(self,userProfile):
        db=DB(self.__tablename__)
        userProfile["created_at"]=datetime.today()
        userProfile["updated_at"]=None
        result=db.create(userProfile)
        del db
        return result

    def update(self,userProfile,id):
        db=DB(self.__tablename__)
        today=datetime.today()
        del userProfile['created_at']
        #userProfile["updated_at"]=today
        result=db.update(userProfile,id)
        del db
        return result

    def delete(self,id):
        db=DB(self.__tablename__)
        result=db.delete(id)
        del db
        return result

    def get_data(self,id):
        db=DB(self.__tablename__)
        fields=["id","user_code","user_name_th","user_name_en","department_code","email","picture","description"]
        result=db.get_data(fields,id)
        return result

    def get_data_by_user_code(self,user_code):
            db=DB()
            sql="SELECT id,\
            user_code,\
            user_name_th,\
            user_name_en,\
            department_code,\
            picture,\
            email,\
            description \
            FROM user_profiles WHERE user_code=%s "
            params=(user_code,)
            results=db.get_specific_sql(sql,None,params)
            del db
            if(len(results)>0):
                result=results[0]
                return result
            return None
