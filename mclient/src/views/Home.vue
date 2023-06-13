<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/vue.svg"> -->
    <!-- <HelloWorld msg="欢迎来到电子工单系统"/> -->
  </div>

  <div>
    <div class="hello">你好，<b>{{ auth.name }}</b></div>
    
    <p class="hello">欢迎来到电子工单系统</p>
    <p class="title">最新公告📣：</p>
    <!-- <div :v-for="noti in auth.notis">{{ noti }}</div> -->
    <!-- <div>{{ auth.notis }}</div> -->
    <div>
    <div class="notice" v-for="item in auth.notis" :key="item">
        {{ item }}
    </div>
  </div>
    <!-- <p>请按照程序发表工单。</p> -->
    <div class="title">能够发起的工单</div>
    <template v-if="auth.workflows">
      <div class="workflow-list">
      <template v-for="wkf in auth.workflows" :key="wkf.id">
        <div class="workflow" >
        {{wkf.id}} {{ wkf.name }}
        <el-button @click="workflow_id_selected = wkf.id">选中</el-button>
      </div>
      </template>
    </div>
    </template>

  </div>
  <div class="fire-new">
    <div class="title fire-elem">新建工单 {{ (typeof(workflow_id_selected) != 'object')?`（选中类型${workflow_id_selected}）`:'（请选择）' }}</div>
    <el-input v-model="fire_title" class="fire-elem" placeholder="请输入标题" />
        <el-button class="fire-btn fire-elem" type="primary" @click="onFireClicked()">发起</el-button>
  </div>
</template>

<script>
import { onMounted,ref} from 'vue'
// @ is an alias to /src
import HelloWorld from '../components/HelloWorld.vue'
import { useAuthStore } from '../stores/auth'
// import { useTicketStore } from '../stores/ticket'
import { useRouter } from 'vue-router'

export default {
    name: 'Home',
    components: {
        HelloWorld 
    },
    setup(){
        const auth = useAuthStore()
        // const ticket = useTicketStore()
        const router = useRouter()

        onMounted(async ()=>{
            await new Promise(r => setTimeout(r, 2000));
            await auth.getnoti()
            auth.getWorkflows()
            // await ticket.getTicketTypes()
        })

        const fire_title = ref('')
        const workflow_id_selected = ref(null)

        const onFireClicked = ()=>{
          if((typeof(workflow_id_selected.value) == 'object'))
            return
          auth.newTicket(workflow_id_selected.value,fire_title.value)
          router.push({name:'AllTicket'})
        }


        return {
            auth,
            workflow_id_selected,
            fire_title,
            onFireClicked
        }
    }
}
</script>

<style scoped>
.title{
  font-size:24px;
  font-weight: bold;
}

.hello{
  font-size:22px;
}

.workflow-list{
  margin-top:20px;
}
.workflow {
  font-size: 24px;
  padding: 8px;
  border-radius: 3px;
  box-shadow: 2px 2px 2px 2px
}

.fire-new{
  border: solid 1px black;
}

.fire-btn{
  width:100%;
}

.fire-elem{
  margin: 10px;
  width:90%;
}

.notice{
  font-size: 20px;
  margin-left: 30px;
  margin-bottom:15px;
}

.notice::before{
  content: '🎈';
}

</style>