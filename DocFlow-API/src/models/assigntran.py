from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from src.util.dbcontroller import DBController as DB

class AssignTranBase(BaseModel):
    document_id:int
    notify_message:str
    assign_from:str
    assign_to:str
    response:str
    stage_at:str
    is_receive:bool
    process_status:str


class AssignTrans(AssignTranBase):


    created_at:datetime=None
    created_at:datetime=None

class AssignTransController():
    __tablename__="assign_trans" 

    def add(self,document):
        db=DB(self.__tablename__)
        document["created_at"]=datetime.today()
        document["updated_at"]=None
        del document["response"]
        result=db.create()
        del db
        return result

    def update(self,document,id):
        db=DB(self.__tablename__)
        today=datetime.today()
        del document['created_at']
        document["updated_at"]=today
        del document["response"]
        result=db.update(document,id)
        del db
        return result

    def update_response(self,response,id):
        db=DB()
        sql="UPDATE assign_trans SET response=%s WHERE id=%s"
        params=(response,int(id),)
        result= db.set_specific_sql(sql,params)
        return result


    def update_stage_at(self,stage_at,id):
        db=DB()
        sql="UPDATE assign_trans SET stage_at=%s WHERE id=%s"
        params=(stage_at,int(id),)
        result= db.set_specific_sql(sql,params)
        return result



    def update_process_status(self,process_status,id):
        db=DB()
        sql="UPDATE assign_trans SET process_status=%s WHERE id=%s"
        params=(process_status,int(id),)
        result= db.set_specific_sql(sql,params)
        return result

    def get_assign_by_id(self,id):
        db=DB()
        sql="SELECT A.id,\
                    A.document_id,\
                    D.document_name,\
                    D.description,\
                    B.user_name_th AS assign_to,\
                    C.user_name_th AS assign_from,\
                    A.created_at,\
                    A.notify_message,\
                    E.status AS process_status\
            FROM \
            assign_trans A INNER JOIN user_profiles B\
                ON A.assign_to =B.user_code \
            LEFT OUTER JOIN user_profiles C\
                ON A.assign_from=C.user_code \
            INNER JOIN  documents D\
                ON A.document_id=D.id\
            INNER JOIN process_status E\
                ON A.process_status=E.code WHERE A.document_id %s\
            AND E.is_process=1 ORDER BY A.id DESC"
        params=(int(id),)
        results=db.get_specific_sql(sql,None,params)
        return results


    def get_assign_by_data(self,sdate,fdate):
        db=DB()
        sql="SELECT A.id,\
                    A.document_id,\
                    D.document_name,\
                    D.description,\
                    B.user_name_th AS assign_to,\
                    C.user_name_th AS assign_from,\
                    A.created_at,\
                    A.notify_message,\
                    E.status AS process_status\
            FROM \
            assign_trans A\
            INNER JOIN user_profiles B\
                ON A.assign_to =B.user_code \
            LEFT OUTER JOIN user_profiles C\
                ON A.assign_from=C.user_code \
            INNER JOIN  documents D\
                ON A.document_id=D.id\
            INNER JOIN process_status E\
                ON A.process_status=E.code\
            WHERE A.created_at BETWEEN (%s AND %s) \
            AND E.is_process=1 ORDER BY A.id DESC"
        params=(sdate,fdate)
        results=db.get_specific_sql(sql,None,params)
        return results




    def delete(self,id):
        db=DB(self.__tablename__)
        result=db.delete(id)
        del db
        return result

    def get_data(self,id):
        db=DB(self.__tablename__)
        result=db.get_data(id)
        return result
