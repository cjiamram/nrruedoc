<template>
<div
    class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0">
    <div class="rounded-t bg-white mb-0 px-6 py-6">
    <div class="text-center flex justify-between">
            <h6 class="text-blueGray-700 text-xl font-bold">ลายเซ็นอิเล็คทรอนิกส์</h6>
    </div>
    </div>
    <div class="flex-auto px-4 lg:px-10 py-10 pt-0 bg-white">
            <div class="flex flex-wrap">
                <div class="w-full lg:w-12/12 px-4">
                    <div class="relative w-full mb-3">
                    <label
                        class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                        >
                        ลายเซ็น
                    </label>
                    <input type="file" class="form-control" ref="fileInputS"  @change="handleFileChange($event, 1)" style="display:none">
                    <a href="#" @click="triggerFileInputSClick"
                    class="bg-lightBlue-600 text-white active:bg-teal-600 font-bold uppercase text-xs px-4 py-3 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150 custom-width">
                    <i class="fa fa-paperclip"></i>&nbsp;แนบไฟล์
                    </a>
                </div>
            <img v-if="this.signatureImg===null"
              src="@/assets/img/ca/Stamp.jpg"  style="width: 250px;" class="rounded-circle img-fluid border border-2 border-white" />
            <img v-else
            :src="this.signatureImg" style="width: 250px;"   class="rounded-circle img-fluid border border-2 border-white" media_type="image/jpeg">
            </div>
            </div>
            <div class="flex flex-wrap">
                <div class="w-full lg:w-12/12 px-4">
                    <div class="relative w-full mb-3">
                    <label
                        class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                        >
                        ตรายางร้องขอ
                    </label>
                    <input type="file" class="form-control" ref="fileInputR"  @change="handleFileChange($event, 2)" style="display:none">
                    <a href="#"    @click="triggerFileInputRClick"
   class="bg-lightBlue-600 text-white active:bg-teal-600 font-bold uppercase text-xs px-4 py-3 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150 custom-width">
   <i class="fa fa-paperclip"></i>&nbsp;แนบไฟล์
</a>

                    
                </div>
                <img v-if="this.stampRequest===null"
              src="@/assets/img/ca/Stamp.jpg"  class="rounded-circle img-fluid border border-2 border-white" style="width: 250px;" />
            <img v-else
            :src="this.stampRequest"  style="width: 250px;"  class="rounded-circle img-fluid border border-2 border-white" media_type="image/jpeg">
                </div>
               
                
            </div>

            <div class="flex flex-wrap">
                <div class="w-full lg:w-12/12 px-4">
                    <div class="relative w-full mb-3">
                    <label
                        class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                        htmlFor="grid-password"
                        >ตรายางอนุมัติ
                        
                    </label>
                    <input type="file" class="form-control" ref="fileInputA"  @change="handleFileChange($event, 3)" style="display:none">
                    <a href="#"  @click="triggerFileInputAClick"
   class="bg-lightBlue-600 text-white active:bg-teal-600 font-bold uppercase text-xs px-4 py-3 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150 custom-width">
   <i class="fa fa-paperclip"></i>&nbsp;แนบไฟล์
</a>

           
                </div>
                <img v-if="this.stampAprove===null"
              src="@/assets/img/ca/Stamp.jpg"  class="rounded-circle img-fluid border border-2 border-white" style="width: 250px;" />
            <img v-else
            :src="this.stampAprove"   class="rounded-circle img-fluid border border-2 border-white" style="width: 250px;" media_type="image/jpeg">
                </div>
             
                
            </div>
           
        
    </div>


</div>
</template>
<script>
import config  from "@/config/config.json";
import swal from 'sweetalert2';
import AuthService from "@/store";
    
export default {
    data(){
        return {
            signature:{
                id:0,
                user_code:AuthService.getUserId(),
                description:'',
                signature:'',
                signature_encoded:'',
                stamp_request:'',
                stamp_accept:'',
                pass_phase:''
            },
            signatureImg:"",
            stampRequest:"",
            stampAprove:""

        }

    },
    mounted(){
        this. getDataByUsercode();
    },
    methods:{

       triggerFileInputSClick() {
          this.$refs.fileInputS.click(); // Trigger click event on the file input
       },

       triggerFileInputRClick() {
          this.$refs.fileInputR.click(); // Trigger click event on the file input
       },

       triggerFileInputAClick() {
          this.$refs.fileInputA.click(); // Trigger click event on the file input
       },

        getPicture(imageName){
           
            const apiUrl=config.apiUrl;
            const url=apiUrl+"signature/get_picture/"+AuthService.getUserId()+"/"+imageName;
            console.log(url);
            return url;
          

       }, 




        async getDataByUsercode(){
            const apiUrl=config.apiUrl;
            const url=apiUrl+"signature/get_data_by_user_code/"+AuthService.getUserId();
            await fetch(url)
                    .then(response => response.json())
                    .then(data => {
                         this.signature=data;
                         //console.log(data);
                        this.signatureImg=this.getPicture(data.signature);
                        this.stampRequest=this.getPicture(data.stamp_request);
                        this.stampAprove=this.getPicture(data.stamp_accept);
                    })
                    .catch(error => {
                        console.error('Error fetching data:', error);
                });

        },

        checkImageSize(file) {
                const maxSizeInBytes = 1 * 1024 * 1024; // 1 MB (adjust this as needed)
                if (file.size > maxSizeInBytes) {
                //console.log('Image size exceeds the maximum limit.');
                return false;
                }
                //console.log('Image size is within the limit.');
                return true;
        },

        async saveSignature(fileUpload,stampType){

            if(fileUpload!==null){
            const apiUrl=config.apiUrl;
            const formData = new FormData();
            formData.append('file', fileUpload);
            const url=apiUrl+'signature/put_stamp/'+AuthService.getUserId()+'/'+stampType;
            await fetch(url, {
                    method: 'POST',
                    body: formData, // Attach the FormData object containing the file
                })
                    .then((response) => {
                    if (response.ok) {
                        const json_data=response.json();
                        console.log(json_data);
                    } else {
                        throw new Error('File upload failed.');
                    }
                    });
            }

        },

        handleFileChange(event,imgType) {
        const flag= this.checkImageSize(event.target.files[0]);
        if(flag===true){
            switch(imgType){
                    case 1:
                        {
                            this.signatureImg=URL.createObjectURL(event.target.files[0]);
                            this.saveSignature(event.target.files[0],1);

                        }
                        break; 
                    case 2:
                        {
                            this.stampRequest=URL.createObjectURL(event.target.files[0]);   
                            this.saveSignature(event.target.files[0],2); 
                        }
                        break;
                    case 3:
                        {
                            this.stampAprove=URL.createObjectURL(event.target.files[0]);   
                            this.saveSignature(event.target.files[0],3); 
                        }
                        break;
                 }   
            }
        else{
            this.$refs.fileInputS.value = '';   
            this.$refs.fileInputR.value = '';   
            this.$refs.fileInputA.value = '';  
            swal.fire({
                    title: 'Error!',
                    text: 'รูปภาพมีขนาดใหญ่เกิน 1 MB',
                    icon: 'error',
                });

            }
        },
    
    }
}
</script>
