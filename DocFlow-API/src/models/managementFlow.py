from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from src.util.dbcontroller import DBController as DB

class ManagementFlowBase(BaseModel):
    document_id:int
    description:str
    department_code:Optional[str]
    status:int
    response:str
    sequence_no:int
    target_user:str

class ManagementFlow(ManagementFlowBase):
    created_at:datetime=None
    updated_at:datetime=None



class ManagementFlowController():
    __tablename__="managements_flow"
    def add(self,document):
        db=DB(self.__tablename__)
        document["created_at"]=datetime.today()
        del document["updated_at"]
        result=db.create()
        del db
        return result

    def update(self,document,id):
        db=DB(self.__tablename__)
        today=datetime.today()
        del document['created_at']
        document["updated_at"]=today
        result=db.update(document,id)
        del db
        return result

    def delete(self,id):
        db=DB(self.__tablename__)
        result=db.delete(id)
        del db
        return result

    def get_data(self,id):
        db=DB(self.__tablename__)
        fields=["id","document_id","description","department_code","status","response","sequence_no"]
        result=db.get_data(fields,id)
        return result

    def update_status(self,status,id):
        db=DB()
        sql="UPDATE managements_flow SET status=%s WHERE id=%s"
        params=(int(status),int(id),)
        result=db.set_specific_sql(sql,params)
        return result

    def update_response(self,status,response,id):
        db=DB()
        sql="UPDATE managements_flow SET status=%s,response=%s WHERE id=%s"
        params=(status,response,int(id),)
        result=db.set_specific_sql(sql,params)
        return result


    def read_data(self,id):
        db=DB()
        sql="SELECT \
                    A.id,\
                    A.description,\
                    B.document_name,\
                    A.response,\
                    A.status,\
                    C.department_name,\
                    A.sequence_no\
            FROM managements_flow A \
            INNER JOIN documents B \
            ON A.document_id=B.id \
            INNER JOIN departments C \
            ON A.department_code=C.department_code \
            WHERE B.document_id=%s \
            ORDER BY A.sequence_no"
        params=(int(id),)
        results=db.get_specific_sql(sql,None,params)
        return results
