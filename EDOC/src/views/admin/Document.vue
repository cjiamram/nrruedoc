<template>
    <div class="flex flex-wrap">
      <div class="w-full lg:w-8/12 px-4">
        <CardDocument :setDocData="setDocData" :clearDoc="clearDoc" :isFilesExist="this.isFilesExist" ref="refDocument" />
      </div>
      <div class="w-full lg:w-4/12 px-4">
        <FileDropzone :getIsExist="getIsExist" ref="refUploadFiles"  />
      </div>
      <div class="w-full lg:w-12/12 px-4">
          <TableDocument ref="refListDocument" :readModify="readModify" :resetFiles="resetFiles" />
      </div>      
    </div>
  
  </template>
  <script>
 import CardDocument from "@/components/Cards/CardDocument.vue";
 import FileDropzone from "@/components/FileManagement/FileDropzone.vue";
 import TableDocument from '@/components/Tables/TableDocument.vue';


  export default {
    data(){
      return {
            docId:0,
            docNo:'',
            isFilesExist:false
      }
    },

    computed: {
    },
    mounted(){

    },

    methods:{

      resetFiles(){
        this.$refs.refDocument.clear();
        this.$refs.refUploadFiles.clearDoc();

      },

      readModify(id){
          this.$refs.refDocument.readModify(id);
          this.$refs.refUploadFiles.readFiles(id);
      },

      setDocData(docNo){
          if(this.isFilesExist===true){
                this.docNo=docNo;
                this.$refs.refUploadFiles.uploadFiles(docNo);
                this.$refs.refListDocument.setDocuments();
          }
      },
      clearDoc(){
          this.$refs.refUploadFiles.clearDoc();
      },
      getIsExist(isExist){
        this.isFilesExist=isExist;
      }

    },

    components: {
            CardDocument,
            FileDropzone,
            TableDocument
    },
  };
  </script>

<style>
  .tab-button {
    padding: 10px 20px;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    cursor: pointer;
  }

  .tab-button.active {
    background-color: #fff;
    border-bottom: 1px solid #fff;
  }

  .tab-content {
    border: 1px solid #ccc;
    padding: 20px;
    margin-top: -1px; /* to align with the border of the active tab */
  }

  .tab-pane {
    display: none;
  }

  .tab-pane.active {
    display: block;
  }
</style>
  
  