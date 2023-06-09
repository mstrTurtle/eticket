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
    <TicketBrief :title="'Ahmad Rajabl'" :desc="'Paid by card'"/>
    <TicketBrief :title="'Humyads Aaskdl'" :desc="'Paid by card'"/>
    <TicketBrief :title="'Paul McCartney'" :desc="'Paid by card'"/>
    <TicketBrief :title="'Ahmad Rajabl'" :desc="'Paid by card'"/>
    <!-- </div> -->
    <!-- <Chats></Chats> -->
</template>

<script setup>
import { reactive } from 'vue'

import TicketBrief from '../components/TicketBrief.vue'

import Card from '../components/Card.vue'

import Chats from '../components/Chats.vue'

// do not use same name with ref
// const form = reactive({
//   name: '',
//   password: ''
// })

const tickets = reactive([{
    id: 1,
    title: "花园水管漏水报修"
},
{
    id: 2,
    title: "采购树苗"
}])

</script>
