<template>
  <div class="con ava">
      <img class="mid avatar"
        src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
        size="large"
        />
    </div>
    <div class="con name">
      John Lennon
    </div>
    <div class="con group">
      Groups: Engineer, Operator
    </div>
    <div class="con logout">
      <el-button class="logout-btn" size="large" @click="this.$router.push({ name: 'Login'})">Logout</el-button>
    </div>
</template>

<script setup lang="ts">

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

}

.logout-btn{
}

</style>