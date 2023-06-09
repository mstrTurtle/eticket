
<template>
  <!-- <div class="screen">

    <div class="back">
      <el-icon color="white"><Icon.ArrowLeftBold style="color:white" /></el-icon>
      Back
    </div>
    <div class="loginBox">
      <div class="title1">欢迎回来</div>

      <input class="inputLine"  />

      <input class="inputLine" type="password" />

      <button class="submitBtn" type="submit">登录</button> 

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
  </div> -->
  
  <LoginForm></LoginForm>
</template>



<script setup>
import { reactive, ref } from 'vue'
import * as Icon from '@element-plus/icons-vue'
import LoginForm from '../components/LoginForm.vue'
import axios from 'axios'

// import jwt from 'jsonwebtoken';

// do not use same name with ref
const form = reactive({
  name: '',
  password: ''
})

const dialogVisible = ref(false)
const loginMessage = ref('')


const onSubmit = () => {
  axios.post('/api/login', {
  })
    .then(response => {
      // Handle response...
      response
    })
    .catch(error => {
      // Handle error...
      error
    });
  login(form.name, form.password)
}

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000'
});

const login = async (email, password) => {
  // 调用登录API获取token

  instance.post('/api/login', { email, password })
    .then(resp => {
      // 生成JWT Token
      // jwt
      // const token = jwt.sign(data, 'secret');

      // 存储Token到本地
      // localStorage.setItem('token', token);

      // console.log(`login token: ${token}`)
      console.log(resp)
      loginMessage.value = `登录成功了, data是：${JSON.stringify(resp.data)}`
      dialogVisible.value = true
    })
    .catch(error => {
      if (error.response.status === 401) {
        loginMessage.value = '登录有问题，账号或者密码错了'
        dialogVisible.value = true
      }
    });


};


</script>

<style scoped>

.title1{
  font-size:2rem;
  padding: 1rem 0px;
}

.screen {
  width: 100vw;
  padding: 0;
  margin: 0;
  height: 100vh;
  font-size: 14px;
  background-position: left top;
  background-color: rgb(231, 169, 169);
  position: relative;
}

.back{
  color:white;
  font-size:2rem;
  padding: 1rem 0px;
  
}

.backIcon{
  color:aliceblue;
}

.loginBox {
  /* width: 480px; */
  height: 280px;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  padding: 2rem;
  opacity: .6;
  border: 2px;
  border-color: red;
  /* background: rgb(206, 110, 110); */

  background-color: rgba(256, 256, 256, .8);
  /* text-align: center; */
}

input.inputLine {
  /* border:none; */
  width: 90%;
  border-width: 0 0 2px 0 ;
  font-size: 2rem;
  margin: 1rem;
  border-color: grey;
}

.inputLine{
  outline: none;
}

.inputLine:hover{
  border-width: 0 0 2px 0 ;
  border-color: rgb(94, 160, 221);
}

.inputLine:focus{
  border-width: 0 0 3px 0 ;
  border-color: green;
}

.submitBtn {
  /* height:auto; */
  background-color: rgb(88, 190, 63);
  color: white;
  width: 90%;
  font-family: '微软雅黑';
  /* font-weight: bold; */
  border:none;
  margin:auto;
  border-radius: .5rem;
  font-size: 2rem;
  height: 3rem
}
</style>