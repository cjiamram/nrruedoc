<template>
    <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded"
        :class="[color === 'light' ? 'bg-white' : 'bg-emerald-900 text-white']">
   <div class="rounded-t mb-0 px-4 py-3 border-0">

    <!-- <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3
            class="font-semibold text-lg"
            :class="[color === 'light' ? 'text-blueGray-700' : 'text-white']"
          >
            เอกสาร
          </h3>
        </div>
      </div> -->
       <div class="block w-full overflow-x-auto">
        <table class="items-center w-full bg-transparent border-collapse">
            <thead>
                <tr>
                    <th style="width:50px"
                    class="px-6 align-middle border border-solid py-3 text-lg uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
              :class="[
                color === 'light'
                  ? 'bg-blueGray-50 text-blueGray-700 border-blueGray-100'
                  : 'bg-emerald-800 text-emerald-300 border-emerald-700',
              ]"
                    >#</th>
                    <th style="width:100px"  class="px-6 align-middle border border-solid py-3 text-lg uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
              :class="[
                color === 'light'
                  ? 'bg-blueGray-50 text-blueGray-700 border-blueGray-100'
                  : 'bg-emerald-800 text-emerald-300 border-emerald-700',
              ]">เลขที่เอกสาร</th>
                    <th  class="px-6 align-middle border border-solid py-3 text-lg uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
              :class="[
                color === 'light'
                  ? 'bg-blueGray-50 text-blueGray-700 border-blueGray-100'
                  : 'bg-emerald-800 text-emerald-300 border-emerald-700',
              ]">หัวข้อ</th>
                    <th style="width:150px"  class="px-6 align-middle border border-solid py-3 text-lg uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
              :class="[
                color === 'light'
                  ? 'bg-blueGray-50 text-blueGray-700 border-blueGray-100'
                  : 'bg-emerald-800 text-emerald-300 border-emerald-700',
              ]">ประเภทเอกสาร</th>
                    <th style="width:200px"  class="px-6 align-middle border border-solid py-3 text-lg uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
              :class="[
                color === 'light'
                  ? 'bg-blueGray-50 text-blueGray-700 border-blueGray-100'
                  : 'bg-emerald-800 text-emerald-300 border-emerald-700',
              ]">หนวยงาน</th>
                    <th style="width:200px"  class="px-6 align-middle border border-solid py-3 text-lg uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left"
              :class="[
                color === 'light'
                  ? 'bg-blueGray-50 text-blueGray-700 border-blueGray-100'
                  : 'bg-emerald-800 text-emerald-300 border-emerald-700',
              ]">จัดการ</th>
                </tr>
            </thead>
            <tbody v-for="(document,index) in this.documents" :key="document.id">
                <tr>
                    <td class="text-center">{{ index+1 }}</td>
                    <td class="text-center">{{ document.document_no }}</td>
                    <td>{{ document.document_name }}</td>
                    <td>{{ document.doc_type }}</td>
                    <td>{{ document.department_name }}</td>
                    <td>
                                <button  @click="this.readDocument(document.id)"
                                        class="bg-lightBlue-500 
                                        text-white 
                                        active:bg-teal-600 
                                        font-bold uppercase text-xs px-4 py-3 rounded shadow 
                                        hover:shadow-md outline-none 
                                        focus:outline-none mr-1 ease-linear transition-all
                                        duration-150"><i class="fa fa-edit"></i>&nbsp;Edit
                                </button>
                                        &nbsp;
                                <button @click="this.confirmDelete(document.id)"
                                        class="bg-red-500 
                                        text-white 
                                        active:bg-red-600 
                                        font-bold uppercase text-xs px-4 py-3 rounded shadow 
                                        hover:shadow-md outline-none 
                                        focus:outline-none mr-1 ease-linear transition-all
                                        duration-150">           
                                        <i class="fa fa-trash"></i>&nbsp;Delete
                                </button>

                    </td>

                </tr>
                
            </tbody>
        </table>
       
       </div>
 
    </div>



</div>
</template>
<script>
import config from '@/config/config.json';
import AuthService from "@/store";
import swal from 'sweetalert2';

export default {
  data() {
    return {
        documents:[],
    };
  },


  mounted(){
    this.setDocuments();
  },
  
  methods:{

    async readDocument(id){
      this.readModify(id);
    },

    async deleteFiles(id){
      const apiUrl=config.apiUrl;
      const url=apiUrl+"document/get_doc_no_by_id/"+id;
      await fetch(url)
              .then(response => {
                if (!response.ok) {
                  throw new Error('Network response was not ok');
                }
                return response.json();
              })
              .then(data => {

                  //console.log(data);
                  
                  const urlDel=apiUrl+"attachment/delete_by_document_id/"+data.document_no;
                  fetch(urlDel)
                    .then(response => {
                      if (!response.ok) {
                            throw new Error('Network response was not ok');
                      }
                      //return response.json();
                    })
                    .then(data => {
                          return  data.Flag;
                    })
                    .catch(error => {
                            console.error('Error fetching data:', error);
                    });


              })
              .catch(error => {
                      console.error('Error fetching data:', error);
              });

    },

    confirmDelete(id){
        //this.deleteDocument(id);

         // console.log(id);

         swal.fire({
          title: 'ต้องการลบข้อมูลหรือไม่?',
          text: 'เมื่อลบข้อมูลแล้วไม่สามารถกู้คืนได้!',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
          if (result.isConfirmed) {
            this.deleteDocument(id);
          }
        });
          
    },

    async deleteDocument(id){
      this.deleteFiles(id);
        const apiUrl=config.apiUrl;
        const url =apiUrl+"document/delete/"+id;
        await fetch(url)
              .then(response => {
                if (!response.ok) {
                  throw new Error('Network response was not ok');
                }
                //return response.json();
              })
              .then(data => {
                 this.setDocuments();        
                
                 this.resetFiles();
                 return  data.Flag;
              })
              .catch(error => {
                      console.error('Error fetching data:', error);
              });

        return false;
     

    },

   

    async setDocuments(){
        const userCode=AuthService.getUserId();
        const apiUrl=config.apiUrl;
        const url=apiUrl+"document/search_doc_by_owner/"+userCode+"/01";
        await fetch(url)
              .then(response => {
                if (!response.ok) {
                  throw new Error('Network response was not ok');
                }
                return response.json();
              })
              .then(data => {
                
                  this.documents=data;
              })
              .catch(error => {
                      console.error('Error fetching data:', error);
              });
    }

  }
  ,
  props: {
    readModify:Function,
    resetFiles:Function,
    color: {
      default: "light",
      validator: function (value) {
        return ["light", "dark"].indexOf(value) !== -1;
      },
    },

    

  },
};
</script>
