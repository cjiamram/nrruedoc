<template>
    <div class="flex flex-wrap">
      <div class="w-full lg:w-8/12 px-4">
        <div class="w-full">
          <CardPersonal/>
        </div>
       
      </div>
      <div class="w-full lg:w-4/12 px-4">
        <CardSignature/>
      </div>
    </div>
  </template>
  <script>
  import CardPersonal from '@/components/Cards/CardPersonal.vue';
  import CardSignature from "@/components/Cards/CardSignature.vue";
  
  
  export default {
    components: {
      CardPersonal,
      CardSignature
    },
  };
  </script>
  