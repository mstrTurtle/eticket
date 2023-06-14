<template>
    <template v-if="ticket.detail">
    

    
    <div class="title">{{ticket.detail.ticket.title}}（id: {{ this.$route.query["id"] }}）</div>
    
    <el-button class="back-btn" @click="router.back()">返回首页</el-button>
    <hr/>
    <el-collapse v-model="activeNames">
      <el-collapse-item class="clps" title="元信息" name="meta">
    <!-- <Edit2></Edit2> -->
    <!-- <StateForm/> -->
    <!-- 1. 元信息部分 -->
    <!-- <div class="sub-title">元信息</div> -->
    <div class="meta-info">
            <!-- <div v-for="(v,k) in ticket.detail.ticket.meta" :key="k">{{ `${k}: ${v}`}}</div> -->
            <div>创建者： {{ ticket.detail.ticket.meta.creator_name }} ( id {{ ticket.detail.ticket.meta.creator_id }} )</div>
            <div>创建时间： {{ timeConvert(ticket.detail.ticket.meta.create_time) }}</div>
            <div>创建时间： {{ timeConvert(ticket.detail.ticket.meta.edit_time) }}</div>
    </div>
    </el-collapse-item>
    <el-collapse-item title="流转历史" name="history">
        <!-- <div class="sub-title">流转历史</div> -->
        <div class="meta-info">
                    <el-timeline>
                        <el-timeline-item
                        v-for="v in ticket.detail.ticket.history_obj"
                        :key="v[3]"
                        :timestamp="timeConvert(v[3])"
                        >
                        {{ `${v[1]} (id ${v[0]}) , ${v[2]}` }}
                        </el-timeline-item>
                    </el-timeline>
        </div>
    </el-collapse-item>
    <!-- <hr/> -->
    <el-collapse-item title="流转进度" name="progress">
    <!-- 2. 流程状态进度展示部分 -->
    <!-- <div class="sub-title">流转进度</div> -->
    <el-steps :active="ticket.detail.state" finish-status="success">
        <el-step v-for="sn in (ticket.detail.state_names)" :key="sn" :title="sn" />
    </el-steps>
    </el-collapse-item>
    <el-collapse-item title="表单" name="form">
    <el-form :model="form" label-width="120px">
     <!-- <hr/> -->
     <!-- 3. 真正表单部分 -->
     <!-- <div class="sub-title">表单</div> -->
     <!-- 对于每个state。注意:set是个trick，只是为了让它执行个语句。 -->
     <div v-for="sn in ticket.detail.state_names" v-bind:key="sn" :se="fields = ticket.detail.form_repr[sn].fields">
        <div >
            <!-- 对于state的每个field -->
            
            <!-- 对于应当填写的state -->
            
            <div v-if="ticket.detail.form_repr[sn].active" class="form-elem current-form">
                <el-form-item v-for="field in fields" v-bind:key="field.name" :label="field.name">
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
                </el-form-item>
            </div>
            <!-- 对于仅为展示作用的state -->
            <div v-if="!ticket.detail.form_repr[sn].active" class="form-elem">
                <el-form-item v-for="field in fields" v-bind:key="field.name" :label="field.name">
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
                </el-form-item>
            </div>
        </div>
    </div>
    <hr/>
    <!-- 4. 转移部分 -->
    <div class="sub-title">等待的转移</div>
    <div class="transitions">
        <el-select v-model="flow_selected" class="m-2" placeholder="请选择一个转移" size="large">
            <el-option v-for="flow_name in ticket.detail.ticket.valid_flow" :key="flow_name" :label="flow_name" :value="flow_name" />
        </el-select>
    </div>
    <hr/>
    <!-- 5. 提交按钮部分 -->
    <el-button type="primary" class="submit-btn" @click="onSubmit">提交表单</el-button>
    
  </el-form>
  
</el-collapse-item>
  
</el-collapse>
  </template>
    <div v-if="ticket.loading">
    加载中...
    </div>
    <CommonModal v-model="ticket.modal" :msg="ticket.info"></CommonModal>
</template>

<script setup>

import { reactive , ref, watch, onMounted} from 'vue'
import Edit2 from '../components/Edit2.vue'
import {useTicketStore} from '../stores/ticket'
import {useRouter, useRoute} from 'vue-router'
import CommonModal from '../components/CommonModal.vue'

const ticket = useTicketStore()

const flow_selected = ref(null)

const activeNames = ref(['form'])

const form = reactive({

})

const router=useRouter()
const route=useRoute()

onMounted(()=>{
            ticket.getTicketDetail(route.query['id']);
        })

function snsConvert(sns){
    var ret = {}
    for(var i = 0; i < sns.length(); i++){
        sn = sns[i]
        ret[i] = sn
    }
    return ret
}

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
    // console.log(detail.form_repr['C'])
    if(!flow_selected.value){
        ticket.modal=true
        ticket.info='请选择flow！'
        return
    }
    else{
        ticket.editTicket(flow_selected.value, router)
    }
}

function timeConvert(ts){
    const d = new Date(ts*1000);
    return `${d.toLocaleString()}`
}

</script>

<style scoped>
.title{
    display:inline-flex;
    font-size: 36px;
}

.back-btn{
    display:inline-flex;
}
.sub-title{
    font-size: 24px;
    margin-bottom:12px;
}
.noting{
    text-align: right;
    color:red;
    font-size:12px
}

>>> .el-collapse-item__header{
    font-size:20px;
    font-weight: bold;
    /* color: red; */
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
    /* border:1px solid black; */
    border-radius:5px;
    padding:10px;
    text-align: center;
    margin-top:30px;
    box-shadow:inset 1px 6px 18px rgba(31, 37, 72, 0.45);
    width: 95%;
}

.current-form{
    box-shadow: 1px 6px 18px rgba(31, 37, 72, 0.45);
    border:none;
}

.submit-btn{
    font-size: 26px;
    height: 50px;
    width:100%;
    align-self: center;
}

</style>