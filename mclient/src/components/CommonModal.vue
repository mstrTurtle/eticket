<template>
    <div v-if="ticket.modal" class="modal">
        <div>{{ ticket.info }}</div>
        <div>
            <el-button @click="ticket.modal=false">好的</el-button>
        </div>
    </div>
</template>

<script setup>

import { useTicketStore } from '../stores/ticket';

const ticket = useTicketStore()

const props = defineProps({
    modelValue:Boolean,
    msg:String
})
</script>

<style scoped>
.modal{
    border: 1px solid black;
}

</style>