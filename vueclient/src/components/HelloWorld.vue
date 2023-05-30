<script setup>
import { ref,reactive, onMounted } from 'vue'
import axios from "axios"
onMounted(() =>{
  axios({
    method:"get",
    url:"http://iwenwiki.com/api/blueberrypai/getChengpinDetails.php"
  }).then(res => {
    console.log(res.data);
  })
})
;
const count = ref(0)
</script>

<template>
  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
  
  </div>
  <el-button type="primary" @click="count--">Primary</el-button>
  
    <el-button type="success" @click="count++">Success</el-button>
  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>

</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>

