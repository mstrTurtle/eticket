<script  setup>
// do not use same name with ref
import { ref } from 'vue'
const isCollapse=ref(true)
function  onLeaveTd() {
    isCollapse.value= true;
}
function onEnterTd() {
    isCollapse.value= false;
}
</script>

<template>
    <el-aside>
        <el-menu router :collapse="isCollapse"  @mouseenter="onEnterTd" @mouseleave="onLeaveTd"  >
            <a href="/" class="logo">
                <img src="../../assets/telecom.png" alt="">
                <h1>中国电信</h1>
            </a>
            <el-menu-item index="/">
                <el-icon ><IEpHouse /></el-icon>
                <span> 主页菜单  </span>
            </el-menu-item>
            <el-menu-item index="/login">
                <el-icon><IEpMenu /></el-icon>
                <span> 权限管理  </span>
            </el-menu-item>
            <el-menu-item>
                <el-icon><IEpMessage /></el-icon>
                <span> 消息通知  </span>
            </el-menu-item>
            <el-menu-item>
                <el-icon><IEpAvatar /></el-icon>
                <span> 用户信息  </span>
            </el-menu-item>
            <el-menu-item>
                <el-icon> <IEpSetting></IEpSetting> </el-icon> 
                <span> 系统设置  </span>
            </el-menu-item>
        </el-menu>
  </el-aside>
</template>

<style lang="scss" scoped>
.el-aside{
    height: 100vh;
    width: auto;
    align-items: center;
}
.el-menu{
    
    width: auto;
    &.el-menu--collapse{
        width:60px;
        & h1{
            display: none;
        }
    }
}
.logo{
    display: flex; 
    justify-content: center;
    align-items: center;
    height: 60px;
    text-decoration: none;
    color:black;
    img{
        width: 32px;
        height: 32px;
    }
}
</style>