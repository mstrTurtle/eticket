<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/vue.svg">
    <!-- <HelloWorld msg="欢迎来到电子工单系统"/> -->
    欢迎来到电子工单系统
  </div>

  <div>
    <p style="font-size: 36px">最新公告：</p>
    <p>请按照程序发表工单。</p>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '../components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
