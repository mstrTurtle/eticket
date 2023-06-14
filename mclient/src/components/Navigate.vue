<template>
    <div class="bottom">
    <el-button class="btn left" @click="this.$router.push({ name: 'Home'})">主页</el-button>
    <el-button class="btn mid" @click="this.$router.push({ name: 'AllTicket'})">所有工单</el-button>
    <el-button class="btn right" @click="this.$router.push({ name: 'MyInfo'})">我的</el-button>
  </div>
</template>

<style scoped>
.bottom{
    position: fixed;
    bottom: 0;
    /* border-top: 1px solid grey; */
    box-shadow: 1px 6px 18px;
    width:98%;
    opacity: 1;
    background-color: white;
    z-index: 999;
}

.btn{
    width: 30%;
    height: 50px;
}

.left{

}
</style>