<script lang="ts" setup>
import axios from 'axios';
import {onBeforeMount, reactive, ref} from 'vue';
const dialogVisible = ref(false)
const loginMessage = ref('')
const tickets=reactive([])
const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers:{
    Authorization : `Bearer ${localStorage.getItem('token')}`
  }
});

const gettickets=async () => {
  instance.get('/tickets')
  .then(resp=>{

    tickets.push(...resp.data)
    console.log(tickets)
  })
  .catch(error=>{
    if (error.response.status === 422) {
        loginMessage.value = '表单获取出错，请重试'
        dialogVisible.value=true
    }
  });
}

onBeforeMount(() => {
  gettickets()
})

</script>

<template>
      <h3>
      ticktesshow
    </h3>
    <div class="ext-large-title">工单列表</div>
    <div v-for="ticket in tickets">
    {{ticket}}
    </div>
    <el-table :data="tickets" border style="width: 100%">
        <el-table-column prop="id" label="ID" width="70" />
        <el-table-column prop="title" label="标题"  />
        <el-table-column fixed="right" label="操作" width="120">
            <template #default>
                <el-button link type="primary" size="small" @click="this.$router.push({ name: 'EditTicket', query: { id: 123 }})">
                    详情
                </el-button>
            </template>
        </el-table-column>
    </el-table>

    <el-dialog v-model="dialogVisible" title="登录小贴士" width="30%" draggable>
    <span>{{ loginMessage }}</span>
    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">
          好的
        </el-button>
      </span>
    </template>
    </el-dialog>
</template>

<style lang="scss" scoped>
</style>