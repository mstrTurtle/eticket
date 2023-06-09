<template>

<div :hidden="!isOpen">
<div
   class="menu-bg" @click="$emit('update:isOpen', false)">
   
</div>
   <el-menu
   class="menu"
    default-active="2"
  >
  <el-menu-item index="2" @click="this.$router.push({ name: 'Home'}); $emit('update:isOpen', false)">
      <el-icon><HomeFilled /></el-icon>
      <template #title>主页</template>
    </el-menu-item>
    <el-sub-menu index="1">
      <template #title>
        <el-icon><Tickets /></el-icon>
        <span>全部工单</span>
      </template>
      
      <el-menu-item-group>
        <template #title><span>工单查询</span></template>
        <el-menu-item index="1-1" @click="this.$router.push({ name: 'AllTicket'})">全部工单</el-menu-item>
        <el-menu-item index="1-2">我能看的</el-menu-item>
      </el-menu-item-group>
      <el-menu-item-group title="工单管理">
        <el-menu-item index="1-3">我发起的</el-menu-item>
      </el-menu-item-group>
      <el-sub-menu index="1-4">
        <template #title><span>工单填写</span></template>
        <el-menu-item index="1-4-1">等待填写的</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>

    <el-menu-item index="3" disabled>
      <el-icon><document /></el-icon>
      <template #title>Navigator Three</template>
    </el-menu-item>
    <el-menu-item index="4" @click="this.$router.push({ name: 'MyInfo'})">
      <el-icon><Avatar /></el-icon>
      <template #title>我的</template>
    </el-menu-item>
  </el-menu>
</div>
</template>
<script setup lang="ts">
import { defineComponent, ref } from 'vue'
import Layout from '../layouts/default.vue'

import {Tickets,HomeFilled, Avatar} from '@element-plus/icons-vue'

import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'

// const isOpen = ref(true)

const props= defineProps({
    isOpen :Boolean
})

const emits = defineEmits([
    'update:isOpen'
])

</script>

<style scoped>

.menu-bg{
    position:fixed;
    width:100vw;
    height:100vh;
    background: grey;
    z-index: 998;
    opacity: .7;
}
.menu{
    position:fixed;
    z-index: 999;
    height:100vh;
    opacity: 1;
}
</style>