from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from src.util.dbcontroller import DBController as DB

class TemplateFlow(BaseModel):
    description:str
    department_code:Optional[str]
    target_user:str
    created_at:datetime=None
    updated_at:datetime=None

class TemplateFlowController():
        __tablename__="template_flow"
        def add(self,templateFlow):
            db=DB(self.__tablename__)
            templateFlow["created_at"]=datetime.today()
            result=db.create()
            del db
            return result

        def update(self,templateFlow,id):
            db=DB(self.__tablename__)
            today=datetime.today()
            del templateFlow['created_at']
            templateFlow["updated_at"]=today
            result=db.update(templateFlow,id)
            del db
            return result

        def delete(self,id):
            db=DB(self.__tablename__)
            result=db.delete(id)
            del db
            return result

        def get_data(self,id):
            db=DB(self.__tablename__)
            fields=["id","description","department_code","created_at","updated_at","target_user"]
            result=db.get_data(fields,id)
            del db
            return result

        def search_data(self,keyword):
            db=DB()
            sql="SELECT \
                A.id,\
                B.department_name,\
                A.description,\
                C.user_name_th\
            FROM template_flow A INNER JOIN departments B \
            ON A.department_code=B.department_code LEFT OUTER JOIN user_profiles C\
            ON A.target_user=C.user_code \
            WHERE CONCAT(B.department_name,' ',A.description,' ',C.user_name_th) LIKE %s"
            keyword="%{keyword}%"
            params=(keyword,)
            results=db.get_specific_sql(sql,None,params)
            return results

        # def get_data(self,id):
        #     db=DB(self.__tablename__)
        #     fields=["id","document_id","description","department_code","status","response","sequence_no"]
        #     result=db.get_data(fields,id)
        #     return result
