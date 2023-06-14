<template>
    <!-- <Card></Card> -->
    <!-- <div class="ext-large-title">工单列表</div>
    <el-table :data="tickets" border style="width: 100%">
        <el-table-column prop="id" label="ID" width="70" />
        <el-table-column prop="title" label="标题" />
        <el-table-column fixed="right" label="操作" width="120">
            <template #default>
                <el-button link type="primary" size="small"
                    @click="this.$router.push({ name: 'EditTicket', query: { id: 123 } })">
                    详情
                </el-button>
            </template>
        </el-table-column>
    </el-table>
    
    <div> -->
        <div style="font-size:36px">所有工单</div>
    <template v-if="ticket.briefs">
        <template v-for="brief in ticket.briefs" :key="brief.id">
            <TicketBrief 
                :title="(brief.overdue?'⚠️':'') + (brief.done?'✅':'') + brief.title" 
                :desc="`${brief.workflow_name} (id ${brief.id})`" 
                :hour="timeHour(brief.meta.edit_time)"
                :ampm="timeAmpm(brief.meta.edit_time)"
                :state="brief.state"
                @click="router.push({name:'EditTicket', query:{id:brief.id}})"
                />
        </template>
    </template>
    <!-- </div> -->
    <!-- <Chats></Chats> -->
</template>

<script setup>
import { reactive , onMounted} from 'vue'

import TicketBrief from '../components/TicketBrief.vue'

import {useTicketStore} from '../stores/ticket'

import { useRouter } from 'vue-router'

import Card from '../components/Card.vue'

import Chats from '../components/Chats.vue'
import { useAuthStore } from '../stores/auth'

// do not use same name with ref
// const form = reactive({
//   name: '',
//   password: ''
// })

const router=useRouter()

const ticket = useTicketStore()

onMounted(()=>{
    ticket.getAllTicket()
})


function timeHour(ts){
    const d = new Date(ts*1000);
    const HH = d.getHours() % 12
    const MM = d.getMinutes()
    const AMPM = d.getHours() < 12 ? 'AM' : 'PM'
    return `${HH}:${MM}`
}

function timeAmpm(ts){
    const d = new Date(ts*1000);
    const HH = d.getHours() % 12
    const AMPM = d.getHours() < 12 ? 'AM' : 'PM'
    return AMPM
}

const tickets = reactive([{
    id: 1,
    title: "花园水管漏水报修"
},
{
    id: 2,
    title: "采购树苗"
}])

</script>
