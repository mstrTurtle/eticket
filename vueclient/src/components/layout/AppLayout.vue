<script  setup>
import AppAside from './APPaside.vue';
import APPHeader from './APPheader.vue'

</script>

<template>
    <div class="common-layout">
      <el-container>
        <AppAside></AppAside>
        <el-container class="header-and-main">
          <APPHeader></APPHeader>
          <el-main>
            <el-scrollbar>
              <router-view></router-view>  
            </el-scrollbar>
          </el-main>
        </el-container>
      </el-container>
      </div>
</template>

  <style scoped>
  .header-and-main {
    flex-direction: column;
    height: 100vh;
  }
  </style>