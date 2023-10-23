from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from src.util.dbcontroller import DBController as DB


class Department(BaseModel):
    department_code:str
    department_name:str
    parent:str
    is_head:int
    created_at:datetime=None
    updated_at:datetime=None


class DepartmentController():
    __tablename__="departments"

    def get_department(self):
        sql="SELECT id,department_code,department_name FROM departments ORDER BY "
        db=DB()
        results=db.get_specific_sql(sql)
        return results

    def get_level_department(self):
        departments=[]
        results=self.get_head_department()
        for dp in results:
            dep={"id":dp["id"],"department_code":dp["department_code"],"department_name":dp["department_name"],"prefix":dp["prefix"],"parent":True}
            departments.append(dep)
            results_child=self.get_child_department(dp["department_code"])
            for dc in results_child:
                dep={"id":dc["id"],"department_code":dc["department_code"],"department_name":dc["department_name"],"prefix":dp["prefix"],"parent":False}

                departments.append(dep)

        return departments

    def get_head_department(self):
        sql="SELECT id,department_code,department_name,prefix FROM departments WHERE is_head=0"
        db=DB()
        results=db.get_specific_sql(sql)
        return results

    def get_child_department(self,head):
        sql="SELECT id,department_code,department_name,prefix FROM departments WHERE is_head=1 AND parent=%s"
        db=DB()
        params=(head,)
        results=db.get_specific_sql(sql,None,params)
        return results

    def get_prefix(self,department_code):
        db=DB()
        sql="SELECT prefix FROM departments WHERE department_code=%s"
        params=(department_code,)
        result=db.get_specific_sql(sql,None,params)[0]
        return result
