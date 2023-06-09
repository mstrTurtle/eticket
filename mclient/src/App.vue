

<template>
  <div id="app">
    <Drawer v-model:is-open="drawerOpen"></Drawer>
    <div class="common-layout">
    <el-container>
      <el-header class="head" >
        <el-row :gutter="8">
        <el-col :sm="3" >
          <el-icon class="xx" size="64px" :color="''" @click="drawerOpen=true">
            <Tickets />
          </el-icon>
        </el-col>
        <el-col :sm="9">
          <h1 class="xx">ETICKET电子工单系统</h1>
        </el-col>
      </el-row>
      <el-row><el-col><p>
      <router-link class="link" to="/">Home</router-link>
    <router-link class="link" to="/about">About</router-link>
    <router-link class="link" to="/login">Login</router-link>
    <router-link class="link" to="/allticket">AllTicket</router-link>
    <router-link class="link" :to="{ name: 'EditTicket', query: { id: 123 }}">EditTicket</router-link>
    <router-link class="link" :to="{ name: 'NewTicket'}">NewTicket</router-link>
    <router-link class="link" :to="{ name: 'MyInfo'}">MyInfo</router-link>
    </p></el-col></el-row>
      
      </el-header>
      <el-container>
        <el-container>
          <el-main>
    <router-view></router-view></el-main>
          <el-footer>By MstrTurtle</el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
    <el-backtop :right="100" :bottom="100" />

  


<!--     
    <Layout>
    </Layout> -->
  </div>
</template>
<script setup lang="ts">
import { defineComponent, ref } from 'vue'
import Layout from './layouts/default.vue'

import {Tickets,HomeFilled, Avatar} from '@element-plus/icons-vue'

import Drawer from './components/Drawer.vue'

import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'


const drawerOpen=ref(false)

defineComponent({Layout})
</script>

<style>
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.xx{

  /* background: purple; */
  min-height: 60px;
  min-width: 9px;
  margin: 2px;
}

.el-row {
  margin-bottom: 20px;
}

.link{
  padding:8px;
}
/* 
html{
  background: grey;
} */

.aside{
  width:fit-content !important;
}

.head{
  height:fit-content !important;
}
</style>