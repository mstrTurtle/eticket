<template>
    <div class="ext-large-title">能够发起的工单</div>
    <el-table :data="tickets" border style="width: 100%">
        <el-table-column prop="id" label="ID" width="70" />
        <el-table-column prop="title" label="标题"  />
        <el-table-column fixed="right" label="操作" width="120">
            <template #default>
                <el-button link type="primary" size="small" @click="this.$router.push({ name: 'EditTicket', query: { id: 123 }})">
                    发起
                </el-button>
            </template>
        </el-table-column>
    </el-table>
  </template>

<script setup>
import { reactive } from 'vue'


// do not use same name with ref
// const form = reactive({
//   name: '',
//   password: ''
// })

const tickets = reactive([{
    id:1,
    title:"报修工单"
},
{
    id:2,
    title:"采购工单"
}])

</script>
