from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from typing import List
from src.util.dbcontroller import DBController as DB

class AttachmentBase(BaseModel):
    document_id:str
    document:str

class Attachment(AttachmentBase):
    update_date:datetime=None


class AttachmentController():
    __tablename__="attachments"

    def add(self,attachment):
        db=DB(self.__tablename__)
        today=datetime.today()
        attachment["update_date"]=today
        result=db.create(attachment)
        del db
        return result

    def update(self,attachement,id):
        db=DB(self.__tablename__)
        result=db.update(attachement,id)
        del db
        return result

    def get_file_name_by_id(self,id):
        db=DB()
        sql="SELECT CONCAT(document_id,'/',document) AS document FROM attachments WHERE id=%s"
        params=(id,)
        results=db.get_specific_sql(sql,None,params)
        #print(results)
        if(len(results)>0):
            return results[0]["document"]
        else:
            return None

    def delete_by_document_id(self,document_id):
        db=DB()
        sql="DELETE FROM attachments WHERE document_id=%s"
        params=(document_id,)
        result=db.set_specific_sql(sql,params)
        del db
        return result

    def delete(self,id):
        db=DB(self.__tablename__)
        result=db.delete(id)
        del db
        return result

    def get_attachments(self,document_id):
        db=DB()
        sql="SELECT id,document_id,document FROM attachments WHERE document_id=%s"
        params=(document_id,)
        results=db.get_specific_sql(sql,None,params)
        return results
