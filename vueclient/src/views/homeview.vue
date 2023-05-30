<script setup>
import { ref,reactive } from 'vue'
defineProps({
  msg: String,
})
const count = ref(100)
const testname = reactive({
  list:["1","2"]
})
</script>

<template>
      <h3>
      HomePage
    </h3>
    
  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
  </div>
  <el-button type="primary" @click="count--">Primary</el-button>
  
    <el-button type="success" @click="count++">Success</el-button>
</template>

<style lang="scss" scoped>
</style>

