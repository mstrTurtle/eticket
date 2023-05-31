<script lang="ts"  setup>
import { useRouter } from 'vue-router';
import axios from 'axios';
import { onBeforeMount,ref } from 'vue';
const router=useRouter()
const username=ref("")
const token=localStorage.getItem('token')
const handleCommand= (command)=>
{
    if (command=="Login")
    {
        router.push("/login")
    }

    if (command=="Logout")
    {
        logout();
        localStorage.setItem('token',"")
        router.push("/login")
    }   
}
const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers:{
    Authorization : `Bearer ${token}`
  }
});

const getme=async () => {
  // 调用登录API获取token
  // instance.post(`/api/login?id=${id}&password=${password}`)
  instance.get('/users/me')
  .then(resp=>{
    // 生成JWT Token
    // const token = jwt.sign(data, 'secret');

    // 存储Token到本地
    // localStorage.setItem('token', token);

    // console.log(`login token: ${token}`)
 // 通过编程式导航跳转到后台主页，路由地址是 /home
    localStorage.setItem('username',resp.data.name)
    localStorage.setItem('groups',resp.data.groups)
    username.value=resp.data.name
    router.push("/")
  })
  .catch(error=>{

  });
}

const logout = async () => {
  // 调用登录API获取token
  // instance.post(`/api/login?id=${id}&password=${password}`)
  instance.post('/api/logout',null)
  .then(resp=>{

  })
  .catch(error=>{
  });
}

onBeforeMount( ()=>{
    getme()
} )

// do not use same name with ref
</script>

<template>
    <el-header>
        <el-icon><IEpCaretRight /></el-icon>
        <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/' }">homepage</el-breadcrumb-item>
            <el-breadcrumb-item> <a href="/">promotion test</a>  </el-breadcrumb-item>
            <el-breadcrumb-item>promotion list</el-breadcrumb-item>
            <el-breadcrumb-item>promotion detail</el-breadcrumb-item>
        </el-breadcrumb>
        
        <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">
            <el-avatar :size="32" :src="'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'" />
            </span>
            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item>{{username}}</el-dropdown-item>
                    <el-dropdown-item command="Login">登录</el-dropdown-item>
                    <el-dropdown-item command="Logout">注销</el-dropdown-item>
                </el-dropdown-menu>
            </template>
        </el-dropdown> 
    </el-header>
</template>

<style lang="scss" scoped>
.el-header{
    background-color:#EBEEF5;
    display:flex;
    align-items: center;
    justify-content: space-between;
}
.el-dropdown{
    margin-left: auto;
}
</style>