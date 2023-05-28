<template>
    <div class="ext-large-title">登录页</div>
  <el-form :model="form" label-width="120px">
    <el-form-item label="账号">
      <el-input v-model="form.name" placeholder="请输入账号" />
    </el-form-item>
    <el-form-item label="密码">
      <el-input v-model="form.password" type="password" placeholder="请输入密码" show-password />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">登录</el-button>
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
.ext-large-title{
    font-size:2lvw
    
}
</style>