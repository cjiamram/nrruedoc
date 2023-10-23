from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from src.util.dbcontroller import DBController as DB


class DocumentType:
    def get_decument_type(self):
        sql="SELECT id,code,doc_type FROM document_type"
        db=DB()
        results=db.get_specific_sql(sql)
        return results
