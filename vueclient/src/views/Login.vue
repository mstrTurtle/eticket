<script lang="ts" setup>
import { ref,reactive } from 'vue'
import { User, Lock } from "@element-plus/icons-vue"
import type { FormRules } from 'element-plus'
import axios from 'axios'
import { useRouter } from 'vue-router';
const form = reactive({
  id: '',
  passwords: '',
})
const dialogVisible = ref(false)
const loginMessage = ref('')
const isloading=ref(false)
const router=useRouter()
const rules=reactive<FormRules>({
  id: [
    { required: true, message: '账号不能为空', trigger: 'blur' },
  ],
  passwords: [
    { required: true, message: '密码不能为空', trigger: 'blur' },
    { min: 3, max: 18, message: 'Length should be 3 to 5', trigger: 'blur'},
  ]
}
)

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000',
});


const login = async (id, password) => {
  // 调用登录API获取token
  // instance.post(`/api/login?id=${id}&password=${password}`)
  instance.post('/api/login',null,{params:{id,password}})
  .then(resp=>{
    // 生成JWT Token
    // const token = jwt.sign(data, 'secret');

    // 存储Token到本地
    localStorage.setItem('token', resp.data.token);
    // console.log(`login token: ${token}`)
    // window.sessionStorage.setItem('token', resp.data.token)
 // 通过编程式导航跳转到后台主页，路由地址是 /home
    loginMessage.value = `登录成功了`
    dialogVisible.value=true
    router.push("/")
  })
  .catch(error=>{
    if (error.response.status === 422) {
        loginMessage.value = '登录有问题，账号或者密码错了'
        dialogVisible.value=true
    }
  });
}

function onSubmit() {
  isloading.value=true;
  login(form.id,form.passwords);
  isloading.value=false;
}
</script>

<template>


  <div class="login">
      
          <el-form :model="form" :rules="rules" label-width="120px" label-position="top">
              <div class="text"><h2>电信工单系统</h2></div>
              <el-form-item label="账号" prop="id">
                <el-input v-model="form.id"  :prefix-icon="User"/>
              </el-form-item>
              <el-form-item label="密码" prop="passwords">
                <el-input v-model="form.passwords"  :prefix-icon="Lock" />
              </el-form-item>
              <el-form-item >
                <el-button type="primary" @click="onSubmit" :loading="isloading">登录</el-button>
            </el-form-item>

         </el-form>
            <el-dialog v-model="dialogVisible" title="登录小贴士" width="30%" draggable>
    <span>{{ loginMessage }}</span>
    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">
          好的
        </el-button>
      </span>
    </template>
    </el-dialog>
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
.text{
  margin-bottom: 10px;
  color:black
}


</style>