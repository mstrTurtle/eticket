
<template>
  <div class="login">
    <div class="mylogin" align="center">
      <h4>登录</h4>
      <el-form
        :model="loginForm"
        :rules="loginRules"
        ref="loginForm"
        label-width="0px"
      >
        <el-form-item label="" prop="account" style="margin-top: 10px">
          <el-row>
            <el-col :span="2">
              <span class="el-icon-s-custom"></span>
            </el-col>
            <el-col :span="22">
              <el-input
                class="inps"
                v-model="form.name" 
                placeholder="请输入账号"
              >
              </el-input>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item label="" >
          <el-row>
            <el-col :span="2">
              <span class="el-icon-lock"></span>
            </el-col>
            <el-col :span="22">
              <el-input
                class="inps"
                v-model="form.password"
                type="password" 
                placeholder="请输入密码" show-password
              ></el-input>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item style="margin-top: 55px">
          <el-button type="primary" round class="submitBtn" @click="onSubmit"
            >登录
          </el-button>
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
  </div>
</template>



<script setup>
import { reactive, ref } from 'vue'

import axios from 'axios'

import jwt from 'jsonwebtoken';

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
    login(form.name,form.password)
}

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000'
});

const login = async (email, password) => {
  // 调用登录API获取token
  
  instance.post('/api/login', { email, password })
  .then(resp=>{
    // 生成JWT Token
    jwt
    // const token = jwt.sign(data, 'secret');

    // 存储Token到本地
    // localStorage.setItem('token', token);

    // console.log(`login token: ${token}`)
    console.log(resp)
    loginMessage.value = `登录成功了, data是：${JSON.stringify(resp.data)}`
    dialogVisible.value=true
  })
  .catch(error=>{
    if (error.response.status === 401) {
        loginMessage.value = '登录有问题，账号或者密码错了'
        dialogVisible.value=true
    }
  });

  
};


</script>

<style scoped>

  .login {
    width: 100vw;
    padding: 0;
    margin: 0;
    height: 100vh;
    font-size: 16px;
    background-position: left top;
    background-color: #242645;
    color: #fff;
    font-family: "Source Sans Pro";
    position: relative;
  }
 
  .mylogin {
    width: 240px;
    height: 280px;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;
    padding: 50px 40px 40px 40px;
    box-shadow: -15px 15px 15px rgba(6, 17, 47, 0.7);
    opacity: 1;
    background: linear-gradient(
      230deg,
      rgba(53, 57, 74, 0) 0%,
      rgb(0, 0, 0) 100%
    );
  }
 
  .inps input {
    border: none;
    color: #fff;
    background-color: transparent;
    font-size: 12px;
  }
 
  .submitBtn {
    background-color: transparent;
    color: #39f;
    width: 200px;
  }

</style>