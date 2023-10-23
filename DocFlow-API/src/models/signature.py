from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from src.util.dbcontroller import DBController as DB
from typing import List


class SignatureBase(BaseModel):
    user_code:str
    description:str
    signature:str
    signature_encoded:str
    stamp_request:str
    stamp_accept:str
    pass_phase:str

class Signature(SignatureBase):
    created_at:datetime=None
    updated_ate:datetime=None

class SignatureController():
    __tableName__="signatures"

    def add(self,signature):
        db=DB(self.__tablename__)
        del document["updated_at"]
        result=db.create(signature)
        del db
        return result

    def isExist(self,user_code):
        db=DB()
        sql="SELECT id FROM signatures WHERE user_code=%s"
        params=(user_code,)
        results=db.get_specific_sql(sql,None,params)
        Flag = True if len(results) > 0 else False
        if Flag==True:
            return {"Flag":True,"id":results[0]["id"]}
        else:
            return {"Flag":False,"id":0}

    def get_id(user_code):
        pass

    def put_stamp(self,file_name,user_code,stamp_type):
        db=DB(self.__tableName__)
        file_info=self.isExist(user_code)
        print(file_info)
        if(not file_info["Flag"]):
            if(stamp_type==1):
                data={"user_code":user_code,"signature":file_name}
            if(stamp_type==2):
                data={"user_code":user_code,"stamp_request":file_name}
            if(stamp_type==3):
                data={"user_code":user_code,"stamp_accept":file_name}
            result=db.create(data)
            del db
            return result
        else:
            if(stamp_type==1):
                data={"user_code":user_code,"signature":file_name}
            if(stamp_type==2):
                data={"user_code":user_code,"stamp_request":file_name}
            if(stamp_type==3):
                data={"user_code":user_code,"stamp_accept":file_name}


            result=db.update(data, file_info["id"])
            del db
            return result







    def update(self,signature,id):
        db=DB(self.__tablename__)
        del document["created_at"]
        result=db.update(signature,id)
        del db
        return result

    def get_data(self,id):
        db=DB(self.__tablename__)
        fields=["id","user_code","description","signature","signature_encoded","stamp_request","stamp_accept","pass_phase"]
        result=db.get_data(signature,fields,id)
        del db
        return result

    def delete(self,id):
        db=DB(self.__tablename__)
        result=db.delete(id)
        return result

    def get_data_by_user_code(self,user_code):
        db=DB()
        sql="SELECT \
            id,\
            user_code,\
            description,\
            signature,\
            signature_encoded,\
            stamp_request,\
            stamp_accept,\
            pass_phase \
        FROM signatures \
        WHERE user_code=%s"
        params=(user_code,)
        results=db.get_specific_sql(sql,None,params)
        if(len(results)>0):
            return results[0]
        return None
