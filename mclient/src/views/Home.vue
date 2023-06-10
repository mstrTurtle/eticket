<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/vue.svg">
    <!-- <HelloWorld msg="欢迎来到电子工单系统"/> -->
    <p style="font-size: 36px">欢迎来到电子工单系统</p>
  </div>

  <div>
    <h2>你好，{{ user.name }}</h2>
    <p style="font-size: 36px">最新公告：</p>
    <!-- <div :v-for="noti in user.notis">{{ noti }}</div> -->
    <!-- <div>{{ user.notis }}</div> -->
    <ol>
    <li style="font-size: 24px" v-for="item in user.notis">
        {{ item }}
    </li>
    </ol>
    <!-- <p>请按照程序发表工单。</p> -->
  </div>
</template>

<script>
import { onMounted } from 'vue'
// @ is an alias to /src
import HelloWorld from '../components/HelloWorld.vue'
import { useAuthStore } from '../stores/auth'

export default {
    name: 'Home',
    components: {
        HelloWorld 
    },
    setup(){
        const user = useAuthStore()

        onMounted(async ()=>{
            await new Promise(r => setTimeout(r, 2000));
            await user.getnoti()
        })


        return {
            user
        }
    }
}
</script>
