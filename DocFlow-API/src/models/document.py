from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from src.util.dbcontroller import DBController as DB
from typing import List

class DocumentBase(BaseModel):
    document_no:str
    document_name:str
    original_department:str
    description:str
    stage_at:str
    doc_type:str
    user_code:str
    priority:str
    document_status:str
    start_date:datetime=None
    due_date:datetime=None

class Document(DocumentBase):
    created_at:datetime=None
    updated_at:datetime=None



class DocumentController():
    __tablename__="documents"

    def add(self,document):
        db=DB(self.__tablename__)
        #document["created_at"]=datetime.today()
        #del document["updated_at"]
        result=db.create(document)
        del db
        return result

    def update(self,document,id):
        db=DB(self.__tablename__)
        today=datetime.today()
        document["updated_at"]=today
        result=db.update(document,id)
        del db
        return result

    def delete(self,id):
        db=DB(self.__tablename__)
        result=db.delete(id)
        del db
        return result

    def extract_text_from_pdf(file_path: str)->List[str]:
        import fitz  # PyMuPDF
        text_content = []
        try:
            with fitz.open(file_path) as pdf_document:
                for page_number in range(pdf_document.page_count):
                    page = pdf_document[page_number]
                    text_content.append(page.get_text())
        except Exception as e:
            return [f"Error reading PDF: {str(e)}"]
        return text_content

    def update_status(self,status,id):
        db=DB()
        sql="UPDATE documents SET document_status=%s WHERE id=%s "
        params=(status,int(id),)
        result=db.set_specific_sql(sql,params)
        del db
        return result

    def update_stage(self,stage,id):
        db=DB()
        sql="UPDATE documents SET stage_at=%s WHERE id=%s "
        params=(stage,int(id),)
        result=db.set_specific_sql(sql,params)
        del db
        return result

    def search_doc_by_owner(self,user_code,status):
        db=DB()
        sql="SELECT DISTINCT A.id,\
                A.document_no,\
                A.document_name,\
                A.description,\
                D.doc_type,\
                A.document_path,\
                C.department_name,\
                A.priority,\
                B.user_name_th AS owner,\
                A.created_at \
        FROM documents A INNER JOIN user_profiles B \
        ON A.user_code=B.user_code \
        INNER JOIN departments C \
        ON A.original_department=C.department_code \
        INNER JOIN document_type D \
        ON A.doc_type=D.code \
        WHERE A.user_code=%s AND A.document_status LIKE %s"
        status=f"%{status}%"
        params=(user_code,status,)
        results=db.get_specific_sql(sql,None,params)
        del db
        return results

    def get_doc_no_by_id(self,id):
        db=DB()
        sql="SELECT document_no FROM documents WHERE id=%s"
        params=(id,)
        results=db.get_specific_sql(sql,None,params)
        if(len(results)>0):
            result=results[0]
            return result
        else:
            return None

    def read_data(self,id):
        db=DB()

        sql="SELECT id,\
                document_no,\
                document_name,\
                original_department,\
                description,\
                stage_at,\
                doc_type,\
                user_code,\
                priority,\
                document_status,\
                start_date,\
                due_date \
        FROM documents WHERE id=%s"
        params=(id,)
        results=db.get_specific_sql(sql,None,params)
        del db
        if(len(results)>0):
            result=results[0]
            return result
        else:
            return None


    def get_max_id(self):
        db=DB()
        sql="SELECT MAX(id) AS MxId FROM documents "
        result=db.get_specific_sql(sql,None,None)
        del db
        if(len(result)>0):
             return result[0]
        else:
             return {"MxId":0}

    def get_prefix(self,department_code):
        db=DB()
        sql="SELECT prefix FROM departments WHERE department_code=%s"
        params=(department_code,)
        result=db.get_specific_sql(sql,None,params)[0]
        return result

    def get_current_year(self):
        current_year = datetime.now().year+543
        return current_year

    def set_counter(self,prefix,current_year):
        db=DB()
        sql="SELECT id FROM doc_run WHERE Prefix=%s AND YearNo=%s"
        params=(prefix["prefix"],current_year,)
        results=db.get_specific_sql(sql,None,params)
        if(len(results)>0):
            sql="UPDATE doc_run SET Running=Running+1 WHERE Prefix=%s AND YearNo=%s"
            result=db.set_specific_sql(sql,params)
            return result
        else:
            sql="INSERT INTO doc_run(Prefix,YearNo,Running) VALUES(%s,%s,1)"
            result=db.set_specific_sql(sql,params)
            return result


    def get_doc_no(self,department_code):
        db=DB()
        prefix=self.get_prefix(department_code)
        current_year=str(self.get_current_year())
        sql="SELECT Running FROM doc_run WHERE Prefix=%s AND YearNo=%s"
        params=(prefix["prefix"],current_year,)
        result=db.get_specific_sql(sql,None,params)
        running=1
        running = (result[0]["Running"] + 1) if len(result) > 0 else 1
        formatted_number = '{:06d}'.format(running)
        self.set_counter(prefix,current_year)
        return {"DocNo":prefix["prefix"]+"-"+formatted_number}

    def get_data(self,id):
        db=DB(self.__tablename__)
        fields=["id",
                "document_no",
                "document_name",
                "document_path",
                "description",
                "original_department",
                "description",
                "stage_at",
                "doc_type",
                "user_code",
                "priority",
                "document_status"]
        result=db.get_data(fields,id)
        del db
        return result
