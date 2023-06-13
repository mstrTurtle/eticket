<template>
  <p style="font-size: 36px">我的</p>
  <div class="con ava">
      <img class="mid avatar"
        src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
        size="large"
        />
    </div>
    <div class="con name">
      {{ auth.$state.name }}
    </div>
    <div class="con group">
      Groups: {{ auth.$state.groups }}
    </div>
    <div class="con logout">
      <el-button class="logout-btn" size="large" @click="this.$router.push({ name: 'About'})">关于此软件</el-button>
    </div>
    <div class="con logout">
      <el-button class="logout-btn" size="large" @click="auth.token=null;this.$router.push({ name: 'Login'})">Logout</el-button>
    </div>
</template>

<script setup lang="ts">

import { useAuthStore } from '../stores/auth';

import { onMounted } from 'vue';

const auth = useAuthStore()

onMounted(()=>{
  auth.getMe()
})

</script>

<style scoped>

.con{
  /* width: 1%; */
  
  justify-content: center;
  display: flex;
}

.ava{
  margin-top: 10px;
  margin-bottom: 40px;
}

.avatar{
  border-radius: 50%;
  width: 30%;
  max-width: 200px;
  box-shadow: 0px 0px 30px 0px black
}

.name{
  font-size: 28px;
  margin-bottom: 20px;
}

.group{
  font-size: 14px;
  margin-bottom: 20px;
}

.logout{
  margin-bottom: 20px;
}

.logout-btn{
}

</style>