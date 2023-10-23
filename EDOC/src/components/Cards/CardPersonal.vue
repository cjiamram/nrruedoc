<template>
    <div
      class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-100 border-0">
      <div class="rounded-t bg-white mb-0 px-6 py-6">
        <div class="text-center flex justify-between">
          <h6 class="text-blueGray-700 text-xl font-bold">ข้อมูลส่วนบุคคล</h6>
          <button
            type="button"
          >
            Settings
          </button>
        </div>
      </div>
      <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
        <form   @submit.prevent="savePersonal">
          <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
            ข้อมูล
          </h6>
          <div class="flex flex-wrap">
            <div class="w-full lg:w-6/12 px-4">
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  Username
                </label>
                <input type="hidden" v-model="this.data.id">
                <input
                  type="text" v-model="this.data.user_code"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  
                />
              </div>
            </div>
            <div class="w-full lg:w-6/12 px-4">
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  Email address
                </label>
                <input
                  type="email"  v-model="this.data.email"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                 
                />
              </div>
            </div>
            <div class="w-full lg:w-6/12 px-4">
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password">
                  ชื่อ-สกุล(ไทย)
                </label>
                <input
                  type="text" v-model="this.data.user_name_th"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                 
                />
              </div>
            </div>
            <div class="w-full lg:w-6/12 px-4">
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                Firstname-Lastname(EN)
                </label>
                <input
                  type="text" v-model="this.data.user_name_en"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                 
                />
              </div>
            </div>
            <div class="w-full lg:w-full px-4">
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  รายละเอียดโดยสังเขบ
                </label>
                <textarea v-model="this.data.description" class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" rows="3">
                </textarea>

              </div>
            </div>
            <div class="w-full lg:w-6/12 px-4">
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                หน่วยงาน
                </label>
                <select v-model="this.data.department_code"  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" >
                <option value="">****เลือกหน่วยงาน****</option>
                        <option v-for="dep in departments" :key="dep.id" :value="dep.department_code">
                                {{ dep.department_name }}
                        </option>
                </select>
              </div>
            </div>
            <div class="w-full lg:w-6/12 px-4">
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                รูปภาพ
                </label>
                <input type="file" style="display:none" ref="fileInput" @change="handleFileChange">
                <a  @click="triggerFileInputClick" href="#"
                        class="bg-blueGray-600 
                        text-white 
                        active:bg-teal-600 
                        font-bold uppercase text-xs px-4 py-3 rounded shadow 
                        hover:shadow-md outline-none 
                        focus:outline-none mr-1 ease-linear transition-all
                        duration-150">
                        <i class="fa fa-camera"></i>&nbsp;แนบรูปภาพ</a>
              </div>
            </div>
            <div class="w-full lg:w-12/12 px-4">
              <div class="relative">
              <img
              alt="..."
              :src="this.personalPhoto"
              class="shadow-xl max-w-200-px max-h-200-px  rounded-full h-auto align-middle border-none"
            
            />
          </div>
            </div>
            <div class="w-full lg:w-12/12 px-4">&nbsp;
            </div>
            <div class="w-full lg:w-12/12 px-4">
                <button  
                        class="bg-teal-500 
                        text-white 
                        active:bg-teal-600 
                        font-bold uppercase text-xs px-4 py-3 rounded shadow 
                        hover:shadow-md outline-none 
                        focus:outline-none mr-1 ease-linear transition-all
                        duration-150">
                        <i class="fa fa-save"></i>&nbsp;บันทึก</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </template>
  
<script>
    import user from "@/assets/img/user.jpg";
    import config from '@/config/config.json';
    import swal from 'sweetalert2';
    import AuthService from "@/store";
    
    export default {
        data(){
            return {
                data:{
                        id:0,
                        user_code: AuthService.getUserId(),
                        user_name_th: '',
                        user_name_en: '',
                        department_code: '',
                        picture: '',
                        description: '',
                        email:'',
                },
                departments:[],
                personalPhoto:user,

            }
        },
        mounted(){
            this.listDepartments();
            this.setDataByUsercode();
        },
        methods:{

          getPicture(imageName){
           
                  const apiUrl=config.apiUrl;
                  const url=apiUrl+"userprofile/get_picture/"+imageName;
                  return url;
                

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
        
        async setDataByUsercode(){
               const apiUrl=config.apiUrl;
               const url=apiUrl+"userprofile/get_data_by_user_code/"+AuthService.getUserId();
               await fetch(url)
                    .then(response => response.json())
                    .then(data => {
                         this.data=data;
                        this.personalPhoto=this.getPicture(data.picture);
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

        getFileExtension() {
                try {
                    //console.log(this.selectedFile);
                    if (this.selectedFile.name !== "") {
                        const file = this.selectedFile.name;
                        const extension = file.split('.').pop();
                        return extension;
                    }
                    return 'jpg';
                } catch (error) {
                    console.error('An error occurred while getting the file extension:', error);
                    return null;
                }
        },
    
        async uploadFile() {
        if(this.selectedFile!==null){
            const apiUrl=config.apiUrl;
            const formData = new FormData();
            formData.append('file', this.selectedFile);
            const extension=this.getFileExtension();
            const url=apiUrl+'userprofile/upload_and_rename/'+AuthService.getUserId()+"."+extension;
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
    
        triggerFileInputClick() {
            this.$refs.fileInput.click(); // Trigger click event on the file input
        },

        handleFileChange(event) {
        const flag= this.checkImageSize(event.target.files[0]);
        this.selectedFile = event.target.files[0];


        if(flag===true){
                this.personalPhoto = URL.createObjectURL(event.target.files[0]);
            }
        else{
            this.$refs.fileInput.value = '';    
            swal.fire({
                    title: 'Error!',
                    text: 'รูปภาพมีขนาดใหญ่เกิน 1 MB',
                    icon: 'error',
                });

            }
        },

        async savePersonal(){
                const apiUrl=config.apiUrl;
                const url= this.data.id===0?apiUrl+"userprofile/add/":apiUrl+"userprofile/update/"+this.data.id;
                const method=this.data.id===0?"POST":"PUT";

                const extension=this.getFileExtension();
                this.data.picture=this.data.user_code+"."+extension;

                fetch(url, {
                    method: method,
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.data),
                    
                })
                .then(response => response.json())
                .then(data => {
                        if(data.Flag===true){
                                this.uploadFile();
                                swal.fire("Success!", "การบันทึกข้อมูลเสร็จสมบูรณ์แล้ว", "success");
                                
                        }
                        else{
                        swal.fire("Error!", "การบันทึกข้อมูลผิดพลาด", "error");
                        }
                })
                .catch(error => {
                                console.error('Error saving data:', error);
                });
                }
        }

    }
</script>
  