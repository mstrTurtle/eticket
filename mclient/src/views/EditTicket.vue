<template>
    <template v-if="ticket.detail">
    <div class="ext-large-title">工单详情页：{{ this.$route.query["id"] }}</div>
    <hr/>
    <!-- <Edit2></Edit2> -->
    <!-- <StateForm/> -->
    <!-- 1. 元信息部分 -->
    <div>元信息</div>
    <div class="meta-info">
            <div v-for="(v,k) in ticket.detail.ticket.meta" :key="k">{{ `${k}: ${v}`}}</div>
    </div>
    <hr/>
    <!-- 2. 流程状态进度展示部分 -->
    <div>流转进度</div>
    <el-steps :active="active" finish-status="success">
        <el-step v-for="sn in ticket.detail.state_names" :key="sn" :title="sn" />
    </el-steps>

    <el-form :model="form" label-width="120px">
     <hr/>
     <!-- 3. 真正表单部分 -->
     <div>表单</div>
     <!-- 对于每个state。注意:set是个trick，只是为了让它执行个语句。 -->
     <div v-for="sn in ticket.detail.state_names" v-bind:key="sn" :se="fields = ticket.detail.form_repr[sn].fields">
        <div class="form-elem" >
            <!-- 对于state的每个field -->
            <el-form-item v-for="field in fields" v-bind:key="field.name" :label="field.name">
                <!-- 对于应当填写的 -->
                <div v-if="ticket.detail.form_repr[sn].active">
                    <div v-if="field.type=='str'">
                        <el-input v-model="ticket.detail.form_repr[sn].model[field.name]" :value="ticket.detail.form_repr[sn].model[field.name]"></el-input>
                    </div>
                    <div v-else-if="field.type=='check'">
                        <el-checkbox v-model="ticket.detail.form_repr[sn].model[field.name]"  :checked="field.value"></el-checkbox>
                    </div>
                    <div v-else-if="field.type=='radio'">
                        <el-radio-group v-model="ticket.detail.form_repr[sn].model[field.name]">
                            <el-radio v-for="selection in field.selections" :key="selection" :label="selection" >{{ selection }}</el-radio>
                        </el-radio-group>
                    </div>
                </div>
                <!-- 对于仅为展示作用的 -->
                <div v-else>
                    <div v-if="field.type=='str'">
                        <el-input  disabled :value="ticket.detail.form_repr[sn].model[field.name]"></el-input>
                    </div>
                    <div v-else-if="field.type=='check'">
                        <el-checkbox  disabled :checked="ticket.detail.form_repr[sn].model[field.name]"></el-checkbox>
                    </div>
                    <div v-else-if="field.type=='radio'">
                        <el-radio-group v-model="ticket.detail.form_repr[sn].model[field.name]">
                            <el-radio v-for="selection in field.selections" :key="selection" :label="selection" disabled>{{ selection }}</el-radio>
                        </el-radio-group>
                    </div>
                </div>
            </el-form-item>
            <div class="noting">{{ticket.detail.form_repr[sn].active?"当前填写位置":""}}</div>
        </div>
    </div>
    <hr/>
    <!-- 4. 转移部分 -->
    <div>等待的转移</div>
    <div class="transitions">
        <el-select v-model="flow_selected" class="m-2" placeholder="Select Me" size="large">
            <el-option v-for="flow_name in ticket.detail.ticket.valid_flow" :key="flow_name" :label="flow_name" :value="flow_name" />
        </el-select>
    </div>
    <hr/>
    <!-- 5. 提交按钮部分 -->
      <el-button type="primary" @click="onSubmit">提交表单</el-button>
  </el-form>
  </template>
    <div v-if="ticket.loading">
    加载中...
    </div>
    <CommonModal v-model="ticket.modal" :msg="ticket.info"></CommonModal>
</template>

<script setup>

import { reactive , ref, watch, onMounted} from 'vue'
import Edit2 from '../components/Edit2.vue'
import StateForm from '../components/StateForm.vue';
import {useTicketStore} from '../stores/ticket'
import {useRouter, useRoute} from 'vue-router'
import CommonModal from '../components/CommonModal.vue'

const ticket = useTicketStore()

const flow_selected = ref(null)

const form = reactive({

})

const router=useRouter()
const route=useRoute()

onMounted(()=>{
            ticket.getTicketDetail(route.query['id']);
        })


// const sns = detail.state_names
// const form_repr = detail.form_repr
// const tkt = detail.ticket

// function getActive(){
//     for(var i=0;i<ticket.blocks.length();i++){
//         if(ticket.blocks[i].active)
//             return i
//     }
//     return 0
// }

const active = ref(1)

const onSubmit=()=>{
    console.log("submit clicked");
    console.log(detail.form_repr['C'])
}

</script>

<style scoped>
.small-caption{
    text-align: left;
    color:black;
}
.noting{
    text-align: right;
    color:red;
    font-size:10px
}

.meta-info{
    /* border:1px solid black; */
    /* border-radius:5px; */
    padding:4px;
    text-align: left;
    margin-top:5px;
    margin-left:10px;
}
.form-elem{
    border:1px solid black;
    border-radius:5px;
    padding:10px;
    text-align: center;
    margin-top:30px;
}

</style>