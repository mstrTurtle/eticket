<script  setup>
import { reactive, useAttrs } from 'vue'
import { User, Lock } from "@element-plus/icons-vue";
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
        <router-link to="/">首页</router-link>
        <router-link to="/login">登录</router-link>
        <el-dropdown>
          <span class="el-dropdown-link">
            <el-avatar :size="32" :src="'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'" />
            </span>
            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item>用户名</el-dropdown-item>
                    <el-dropdown-item>Action 2</el-dropdown-item>
                    <el-dropdown-item divided>注销</el-dropdown-item>
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