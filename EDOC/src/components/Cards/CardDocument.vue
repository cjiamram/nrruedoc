<template>



<div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0">
    <div class="rounded-t bg-white mb-0 px-6 py-6">
      <div class="text-center flex justify-between">
        <h6 class="text-blueGray-700 text-xl font-bold">สร้างเอกสาร</h6>
      </div>
    </div>

    <div class="flex-auto px-2 lg:px-2 py-4 pt-1">
      <form   @submit.prevent="saveDocument">
      
        <div class="row">
          <!-- <div class="flex flex-wrap"> -->
        <div class="card flex flex-wrap">
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                หน่วยงาน
              </label>
          
              <select  @change="setDocNo"  
              class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" v-model="document.original_department" >
                <option value="">****เลือกหน่วยงาน****</option>

                <option v-for="dep in departments" :key="dep.id" :value="dep.department_code">
                        {{ dep.department_name }}
                </option>

              </select>
            </div>
          </div>
          
          <div class="w-full lg:w-4/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                เลขที่เอกสาร
              </label>
              <input type="hidden" id="id" v-model="document.id">
              <input
                type="text"
                v-model="document.document_no" required
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              
              />
            </div>
          </div>
          <div class="w-full lg:w-8/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                หัวข้อเอกสาร
              </label>
              <input
                type="text" 
                v-model="document.document_name"
                class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              
              />
            </div>
            
          </div>
          <div class="w-full lg:w-12/12 px-4">
            <div class="relative w-full mb-3">
              <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                รายละเอียด
              </label>
           
              <textarea rows="4" v-model="document.description" class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"></textarea>
            </div>
            
          </div>
          <div class="w-full lg:w-4/12 px-4">
            <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                ประเภทเอกสาร
              </label> 
            <select  v-model="document.doc_type"  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150">
                <option value="">***ประเภทเอกสาร***</option>
                <option v-for="item in documentTypes" :key="item.id" :value="item.code">
                                            {{ item.doc_type }}
                </option>

            </select>
          </div>
          <div class="w-full lg:w-4/12 px-4">
            <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                วันที่
              </label>
              <input type="date" id="datepicker" v-model="document.created_at"  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" placeholder="Select a date" >

          </div>
          <div class="w-full lg:w-4/12 px-4">
            <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
                ระดับความสำคัญ
              </label>
              <select 
              id="priority"
              v-model="document.priority" required
              class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150">
                <option value="">***ระดับความเร่งด่วน***</option>
                <option value="01">ปกติ</option>
                <option value="02">เร่งด่วน</option>
                <option value="03">เร่งด่วนมาก</option>
            </select>
          </div>
          <div class="w-full lg:w-4/12 px-4">
            <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >
              วันที่เริ่มดำเนินการ
                
              </label>
              <input type="date" id="datepicker" v-model="document.start_date"  
              class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" 
              placeholder="Select a date" >


          </div>
          <div class="w-full lg:w-4/12 px-4">
            <label
                class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                htmlFor="grid-password"
              >วันหมดอายุ
              
              </label>
              <input type="date" id="datepicker" v-model="document.due_date"  
              class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" 
              placeholder="Select a date" >


          </div>
          <div class="w-full lg:w-4/12 px-4">

        </div>

          <div class="w-full lg:w-12/12 px-4">
            <br/>
            <button 
            class="bg-teal-500 
            text-white 
            active:bg-teal-600 
            font-bold uppercase text-xs px-4 py-3 rounded shadow 
            hover:shadow-md outline-none 
            focus:outline-none mr-1 ease-linear transition-all
            duration-150"
> <i class="fa fa-save"></i>&nbsp;Save</button>&nbsp;
<a href="#"
            class="bg-lightBlue-500 
            text-white 
            active:bg-lightBlue-600 
            font-bold uppercase text-xs px-4 py-3 rounded shadow 
            hover:shadow-md outline-none 
            focus:outline-none mr-1 ease-linear transition-all
            duration-150" @click="clear">
            <i class='fas fa-book-medical'></i>&nbsp;Clear</a>

          </div>
          </div>
        </div>


         
      </form>
    </div>
</div>  


</template>

<script>
import config from '@/config/config.json';
import swal from 'sweetalert2';
import AuthService from "@/store";


export default {
  data(){
    return {
      document: {
                    id:0,
                    document_no: '',
                    document_name: '',
                    original_department: '',
                    description: '',
                    stage_at: '',
                    doc_type: '01',
                    user_code: AuthService.getUserId(),
                    priority: '01',
                    document_status: '01',
                    created_at:this.getCurrentDate(),
                    start_date:this.getCurrentDate(),
                    due_date:this.getDueDate(30)
      },

      departments:[],
      documentTypes:[],
      priority:[]
    }
  },
  components:{
  },
  props:{
    setDocData:Function,
    isFilesExist:Boolean,
    clearDoc:Function 
  },
  mounted(){
    this.listDocumentTypes();
    this.listDepartments();
  }
  ,
  methods: {
    clear(){
      this.document= {
                    id:0,
                    document_no: '',
                    document_name: '',
                    original_department: '',
                    description: '',
                    stage_at: '',
                    doc_type: '01',
                    user_code: AuthService.getUserId(),
                    priority: '01',
                    document_status: '01',
                    created_at:this.getCurrentDate(),
                    start_date:this.getCurrentDate(),
                    due_date:this.getDueDate(30)
      }
      this.clearDoc();

    },
    async readModify(id){
        const apiUrl=config.apiUrl;
        const url=apiUrl+"document/read_data/"+id ;

        await fetch(url)
              .then(response => {
                if (!response.ok) {
                  throw new Error('Network response was not ok');
                }
                return response.json();
              })
              .then(data => {
                      this.document={
                        id:data.id,
                        document_no: data.document_no,
                        document_name: data.document_name,
                        original_department: data.original_department,
                        description: data.description,
                        stage_at: '',
                        doc_type: data.doc_type,
                        user_code: AuthService.getUserId(),
                        priority: data.priority,
                        document_status: '01',
                        created_at:this.getCurrentDate(),
                        start_date:this.getCurrentDate(),
                        due_date:this.getDueDate(30)
                      } 

              })
              .catch(error => {
                      console.error('Error fetching data:', error);
            });
        


    },

    getCurrentDate() {
            const today = new Date();
            const year = today.getFullYear();
            const month = String(today.getMonth() + 1).padStart(2, '0');  // Months are zero-indexed
            const day = String(today.getDate()).padStart(2, '0');
            return `${year}-${month}-${day}`;
    },

    getDate(cdate){
            const year = cdate.getFullYear();
            const month = String(cdate.getMonth() + 1).padStart(2, '0');  // Months are zero-indexed
            const day = String(cdate.getDate()).padStart(2, '0');
            return `${year}-${month}-${day}`;
    },

    getDueDate(range){
            // Assuming you have a starting date
            const startingDate = new Date(); // Create a new Date object with the current date and time
            const numberOfDaysToAdd = range;
            const endingDate = new Date(startingDate);
            endingDate.setDate(startingDate.getDate() + numberOfDaysToAdd);
            const dueDate=this.getDate(endingDate);
            return dueDate;
    },
    getMaxId(){
            const apiUrl=config.apiUrl;
            const url=apiUrl+"document/get_max_id/";

            fetch(url)
              .then(response => {
                if (!response.ok) {
                  throw new Error('Network response was not ok');
                }
                return response.json();
              })
              .then(data => {
                      this.document.id=data.MxId;
                      return data.MxId;
              })
              .catch(error => {
                      console.error('Error fetching data:', error);
              });
    },
    setDocNo(event){
              const apiUrl=config.apiUrl;
              const url=apiUrl+"document/get_doc_no/"+event.target.value;
              //console.log(url);

              fetch(url)
                .then(response => {
                  if (!response.ok) {
                    throw new Error('Network response was not ok');
                  }
                  return response.json();
                })
                .then(data => {
                        //console.log(data);
                        this.document.document_no=data.DocNo;     
                })
                .catch(error => {
                        console.error('Error fetching data:', error);
                });
    },

    saveDocument() {

          if(this.isFilesExist===true){

          const apiUrl=config.apiUrl;
          const url= this.document.id===0?apiUrl+"document/add/":apiUrl+"document/update/"+this.document.id;
          const method=this.document.id===0?"POST":"PUT";
          this.document.start_date+="T00:00:00.0000",
          this.document.due_date+="T00:00:00.0000"
          fetch(url, {
                method: method,
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.document),
                
            })
            .then(response => response.json())
            .then(data => {
                    if(data.Flag===true){
                            this.setDocData(this.document.document_no);
                            this.clear();
                            swal.fire("Success!", "การบันทึกข้อมูลเสร็จสมบูรณ์แล้ว", "success");
                            
                    }
                    else{
                     swal.fire("Error!", "การบันทึกข้อมูลผิดพลาด", "error");
                    }
            })
            .catch(error => {
                            console.error('Error saving document:', error);
            });
          }else{
            swal.fire("Error!", "กรุณาแนบเอกสาร", "error");

          }
    },
        
    async listDocumentTypes(){
                    const apiUrl=config.apiUrl;
                    const url= apiUrl+"documentType/get_decument_type/";
                    await fetch(url)
                    .then(response => response.json())
                    .then(data => {
                         this.documentTypes=data;
                    })
                    .catch(error => {
                        console.error('Error fetching data:', error);
                    });
        },

        async listDepartments(){
                    const apiUrl=config.apiUrl;
                    const url= apiUrl+"department/get_level_department/";
                    await fetch(url)
                    .then(response => response.json())
                    .then(data => {
                         this.departments=data;
                    })
                    .catch(error => {
                        console.error('Error fetching data:', error);
                    });
        },
  }
};
</script>

<style scoped>


</style>





