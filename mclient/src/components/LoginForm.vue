<template>
    <!-- Designed by Jaysen Henderson. Developed by me for fun. Source: https://dribbble.com/shots/3686055-hello-login-Ui -->

<div class="wrapper">
  
  <!--  Header  -->
  <header class="section header">
    <div class="trapezoid"></div>
    
    <div class="header__text">
      <h1>ETICKET 工单系统</h1>
      <p>请登录或联系管理员获得账户.</p>
    </div>
  </header>


    
    <!--  Sign In  -->
    <section class="section sign-in">
      <div class="form">
        <input v-model="id" type="text" name="email" placeholder="账户ID">
        <input v-model="password" type="password" name="password" placeholder="密码">
        <button @click="onLoginClicked">登录</button>
      </div>
    </section>
</div>

<div v-if="auth.loading">
    加载中...
  </div>
  <div v-if="auth.modal">
    <div>
      {{ auth.info }}
    </div>
    <div>
      <el-button @click="auth.modal=false"></el-button>
    </div>
  </div>
  
</template>

<script setup>
import { reactive ,ref } from 'vue'
import {useAuthStore} from '../stores/auth.ts'
import {useRouter} from 'vue-router'

const router=useRouter()

const auth = useAuthStore()

const id=ref(null)
const password=ref(null)


function onLoginClicked(){
  if(!id.value || !password.value){
    auth.modal=true
    auth.info="不对"
  }
  auth.login(id.value,password.value)
  if(auth.token) 
    router.push({ name: 'Home'})
}

</script>

<style lang="scss" scoped>


// Colors
$c-blue: #1126be;
$c-white: #fefefe;

// Transparent Colors
$t-blue: rgba(17, 38, 190, 0.8);

// Gradients
$g-blue: linear-gradient($t-blue, $t-blue);

// Shadows
$s-basic: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);


// Imports
@import url('https://fonts.googleapis.com/css?family=Nunito:300');


// Resets
* {
  box-sizing: border-box;  
  font-family: inherit;
}


body {
  margin: 0;  
  // padding-bottom: 20px;
  font-family: 'Nunito', sans-serif;
  color: $c-white;
  background: $c-white;
}


// Global Layout
.wrapper {
  margin: 0 auto;
  max-width: 1080px;
  // box-shadow: $s-basic;
}

.section {
  padding: 1rem;
}

// Header Styles
.header {
  position: relative;
  text-align: center;
  
  &__text {
    position: relative;
    padding: 3.5rem 0 7rem ;
    
    > h1 {
      margin: 0;
      font-size: 2.5rem;
    }
  }
  
  > .trapezoid {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transform: skewY(-10deg);
    transform-origin: top left; 
    box-shadow: $s-basic;
    background: $g-blue;
    background-position: top center;
    background-attachment: fixed;
  }
}

// Form, input and button styles
.form {
  margin: 0 auto;
  max-width: 17rem;
  overflow: auto;
  
  > * + * {
    margin-top: 1rem;
  }
  
  > input {
    border: 0;
    border-bottom: 1px solid $c-blue;
    border-radius: 0;
    width: 100%;
    height: 2rem;
    padding: 0 0 0.25rem 0;
    font-size: 1rem;
    color: $c-blue;
    background: $c-white;

    &:focus {
      outline: none;
    }

    &::placeholder {
      color: $c-blue;
    }
  }
  
  > button {
    margin-top: 2rem;
    border: 0;
    border-radius: 200px;
    width: 100%;
    padding: 0.85rem;
    font-size: 1rem;
    color: $c-white;
    background: $c-blue;

    &:focus {
      outline: none;
    }  
  }
  
  > p {
    margin: 0.25rem 0 0;
    text-align: center;
    color: $c-blue; 
  }
}

// Starting value for sign-up form
.sign-up {
  display: none;
}

// Switch btn: there are two only because I was in a hurry a didn't want to write all the javascript immediately. In a production environment, there would be one opposite btn class that switched between the two.
.opposite-btn1,
.opposite-btn2 {
  cursor: pointer;
}

</style> 