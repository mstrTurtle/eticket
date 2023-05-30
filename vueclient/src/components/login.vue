<script  setup>
import { ref,reactive } from 'vue'
import { User, Lock } from "@element-plus/icons-vue"
const form = reactive({
  name: '',
  passwords: '',
})
const isloading=ref(false)
function onSubmit() {
  isloading.value=true;
  console.log('submit!');
  isloading.value=false;
}
</script>

<template>


  <div class="login">

          <el-form :model="form"  label-width="120px" label-position="top">
              <el-form-item label="账号" >
                <el-input v-model="form.name" prop="name" :prefix-icon="User"/>
              </el-form-item>
              <el-form-item label="密码">
                <el-input v-model="form.passwords" prop="passwords" :prefix-icon="Lock" />
              </el-form-item>
              <el-form-item >
                <el-button type="primary" @click="onSubmit" :loading="isloading">登录</el-button>
            </el-form-item>

         </el-form>
        
</div>
      

    
</template>

<style lang="scss" scoped>
.login{
  background-image: url("/src/assets/background.png");
  background-size: 100% 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  @keyframes animated-border {
  0% {
    box-shadow: 0 0 0 0 rgba(255,255,255,0.4);
  }
  100% {
     box-shadow: 0 0 0 20px rgba(255,255,255,0);
  }
}
  .el-form{
    animation: animated-border 1.5s infinite;
  font-family: Arial;
  font-size: 18px;
  line-height: 30px;
  font-weight: bold;
  color: white;
  border: 2px solid;
  border-radius: 10px;

    width: 300px ;
    padding: 30px;
    border-radius: 10px;
    background-color: #FFF;
  }
}

// Hover styles

.el-button {
  
}


</style>