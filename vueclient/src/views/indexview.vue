<script setup>
import { ref,reactive } from 'vue'
defineProps({
  msg: String,
})
const count = ref(100)

</script>

<template>
      <h3>
      HomePage
    </h3>
    
  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
  </div>
  <el-button type="primary" @click="count--">-</el-button>
  
    <el-button type="success" @click="count++">+</el-button>
</template>

<style lang="scss" scoped>
</style>

