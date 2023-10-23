<template>
    
<div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0">
    <div class="rounded-t bg-white mb-0 px-6 py-6">
      <div class="text-center flex justify-between">
       <button  class="px-4 py-2 bg-emerald-600 text-white rouded-lg hover:bg-red-600"  @click="triggerFileInputClick"><i class='fas fa-clipboard'></i>&nbsp;เลือกไฟล์</button>
      </div>
    </div>

    <div class="drop-zone" @dragover.prevent="handleDragOver" @drop="handleDrop">
      <p>Drag and drop files here or click to select</p>
      <input type="file"  style="display: none"  ref="fileInput" @change="handleFileChange" >
      <div class="card p-4 border border-gray-300 rounded">
        <div class="flex flex-wrap -mx-2" >
      
        <table class="border border-gray-300 p-2 w-full">
          <tr v-for="item in documentFiles" :key="item.id">
            
            <td class="p-2 border w-custom">
              <a><img src="@/assets/img/fileicon/pdf.png" class="max-w-36 h-auto"/>
              </a>
              
            </td>
            <td class="p-2 border">
              <p class="text-emerald-500">{{ item.docName }}</p>
            <button v-if="item.typeStatus===0" @click="deleteItem(item.id)" class="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600">
              <i class="fa fa-times"></i>&nbsp;Delete
            </button>
            <button v-else @click="deleteItemOnDb(item.id,item.fileId)" class="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600">
              <i class="fa fa-times"></i>&nbsp;Delete
            </button>

          </td>
            
          </tr>
        </table>
      </div>
      </div>
    </div>
  
</div>
  </template>
  
  <script>
  import config from '@/config/config.json';
  export default {
    data(){
      return {
        documentFiles:[],
      }
    },

    props:{
        docId:{
            type:Number,
            default:0,           
        },
        getIsExist:Function 
        
    },
    methods: {

      getAttachments(documentId){
          return documentId;
      },
      
      clearDoc(){
        this.documentFiles=[];
      },
      
      docExist(){
          const isExist=this.documentFiles.length>0?true:false;
          return isExist;
      },
      
      triggerFileInputClick() {
          this.$refs.fileInput.click(); // Trigger click event on the file input
      },

      async deleteItemOnDb(itemId,fileId){
         
          const apiUrl=config.apiUrl;
          const url=apiUrl+"attachment/delete/"+fileId;
          await fetch(url)
            .then(response => {
              if (!response.ok) {
                    throw new Error('Network response was not ok');
              }
                 return response.json();
            })
            .then(data => {
                console.log(data);
                this.deleteItem(itemId);
                    
            })
            .catch(error => {
                    console.error('There was an error with the request:', error);
            });
      },

      deleteItem(itemId) {
        this.documentFiles.splice(itemId, 1);
        this.setIndex();
      },

      getFileExtension(filename) {
            return filename.split('.').pop().toLowerCase();
      },

      async handleDragOver(event) {
        event.preventDefault();
      },
      async handleDrop(event) {
        event.preventDefault();
        const files = event.dataTransfer.files;
        await this.handleFilesUpload(files);
      },
      async setIndex(){
        for (let i = 0; i < this.documentFiles.length; i++){
          this.documentFiles.id=i;
        }
        const isExist=this.documentFiles.length>0?true:false;
        this.getIsExist(isExist);
      },
      async readFiles(id){
            this.documentFiles=[];
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

                    this.readFromDb(data.document_no);
            })
            .catch(error => {
                    console.error('There was an error with the request:', error);
            });
          
            
      }
      ,
      async readFromDb(docNo){
          
          const apiUrl=config.apiUrl;
          const url=apiUrl+"attachment/get_attachments/"+docNo;
          await fetch(url)
            .then(response => {
              if (!response.ok) {
                    throw new Error('Network response was not ok');
              }
                 return response.json();
            })
            .then(data => {

              data.forEach((item, index) => {
                    const objFile={"id":index,"fileId":item.id,"docFile":item.document,"docName":item.document,"docType":"pdf","typeStatus":1};
                    this.documentFiles.push(objFile);
                   
              });
              this.setIndex();
                    
                  
            })
            .catch(error => {
                    console.error('There was an error with the request:', error);
            });

      },
      

      appendDocumentFiles(files){
        for (let i = 0; i < files.length; i++) {
            const docFile=files[i];
            const docType=this.getFileExtension(docFile.name);
            const docName=files[i].name;
            const objFile={"id":i,"docFile":docFile,"docName":docName,"docType":docType,"typeStatus":0};
            this.documentFiles.push(objFile);
        }
        this.setIndex();
      },

      async handleFilesUpload(files){
        this.appendDocumentFiles(files);
      }
      ,
      async handleFileChange(event) {
        const files = event.target.files;
        this.appendDocumentFiles(files);
      },

      async addAttachment(file){
         const apiUrl=config.apiUrl;
         const url=apiUrl+"attachment/add";

          const data = {
            document_id: this.docId,
            document: file
          };

          const requestOptions = {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
          };

          try {
                    const response = await fetch(url, requestOptions);
                    if (!response.ok) {
                      throw new Error('Network response was not ok');
                    }
                    const responseData = await response.json();
                    console.log('Response data:', responseData);
            } catch (error) {
                    console.error('Error posting data:', error);
            }


      },

      async uploadFiles(docNo){
            this.documentFiles.forEach(document => {
                if(document.typeStatus===0){
                    this.uploadFile(document.docFile,docNo);
                    this.saveAttachment(document.docName,docNo);
                }
            });

      },

      async saveAttachment(document,docNo){
              const attachment={
                    "document_id":docNo,
                    "document":document
              }
              console.log(attachment);
              const apiUrl=config.apiUrl;
              const url=apiUrl+'attachment/add/';  // Replace with your API endpoint

              await fetch(url, {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',  // Adjust content type based on your API requirements
                },
                body: JSON.stringify(attachment),
              })
                .then(response => {
                        if (!response.ok) {
                          throw new Error('Network response was not ok');
                        }
                        return response.json();
                })
                .then(data => {
                          // Handle the API response data
                          console.log('API response:', data);
                })
                .catch(error => {
                          // Handle errors
                          console.error('Error:', error);
                });
      },


      async uploadFile(file,docNo) {
      if(this.selectedFile!==null){
          const apiUrl=config.apiUrl;
          const formData = new FormData();
          formData.append('file', file);
          const url=apiUrl+'document/upload_doc/'+docNo;
          await fetch(url, {
                      method: 'POST',
                      body: formData, // Attach the FormData object containing the file
              })
                .then((response) => {
                  if (response.ok) {
                          // const json_data=response.json();
                          // console.log(json_data);
                         
                  } else {
                          throw new Error('File upload failed.');
                  }
                });
          }
    },
    }
  };
  </script>
  
  <style scoped>
  .drop-zone {
    border: 2px dashed #ccc;
    padding: 20px;
    text-align: center;
    cursor: pointer;
    height: 520px;
    max-height: 520px;
    overflow-y: scroll;
    
  }
  
  .drop-zone p {
    margin: 0;
  }
  
  .drop-zone:hover {
    background-color: #f0f0f0;
  }


  .w-custom {
    width: 100px;
  }
</style>



  