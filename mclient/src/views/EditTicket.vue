<template>
    <div class="ext-large-title">工单详情页：{{ this.$route.query["id"] }}</div>
    <hr/>
    <!-- <Edit2></Edit2> -->
    <!-- <StateForm/> -->
    <!-- 1. 元信息部分 -->
    <div>元信息</div>
    <div class="meta-info">
            <div v-for="(v,k) in tkt.meta" :key="k">{{ `${k}: ${v}`}}</div>
    </div>
    <hr/>
    <!-- 2. 流程状态进度展示部分 -->
    <div>流转进度</div>
    <el-steps :active="active" finish-status="success">
        <el-step v-for="sn in sns" :key="sn" :title="sn" />
    </el-steps>

    <el-form :model="form" label-width="120px">
     <hr/>
     <!-- 3. 真正表单部分 -->
     <div>表单</div>
     <!-- 对于每个state。注意:set是个trick，只是为了让它执行个语句。 -->
     <div v-for="sn in sns" v-bind:key="sn" :se="fields = frp[sn].fields">
        <div class="form-elem" >
            <!-- 对于state的每个field -->
            <el-form-item v-for="field in fields" v-bind:key="field.name" :label="field.name">
                <!-- 对于应当填写的 -->
                <div v-if="frp[sn].active">
                    <div v-if="field.type=='str'">
                        <el-input v-model="frp[sn].model[field.name]" :value="frp[sn].model[field.name]"></el-input>
                    </div>
                    <div v-else-if="field.type=='check'">
                        <el-checkbox v-model="frp[sn].model[field.name]"  :checked="field.value"></el-checkbox>
                    </div>
                    <div v-else-if="field.type=='radio'">
                        <el-radio-group v-model="frp[sn].model[field.name]">
                            <el-radio v-for="selection in field.selections" :key="selection" :label="selection" >{{ selection }}</el-radio>
                        </el-radio-group>
                    </div>
                </div>
                <!-- 对于仅为展示作用的 -->
                <div v-else>
                    <div v-if="field.type=='str'">
                        <el-input  disabled :value="frp[sn].model[field.name]"></el-input>
                    </div>
                    <div v-else-if="field.type=='check'">
                        <el-checkbox  disabled :checked="frp[sn].model[field.name]"></el-checkbox>
                    </div>
                    <div v-else-if="field.type=='radio'">
                        <el-radio-group :v-model="frp[sn].model[field.name]">
                            <el-radio v-for="selection in field.selections" :key="selection" :label="selection" disabled>{{ selection }}</el-radio>
                        </el-radio-group>
                    </div>
                </div>
            </el-form-item>
            <div class="noting">{{frp[sn].active?"当前填写位置":""}}</div>
        </div>
    </div>
    <hr/>
    <!-- 4. 转移部分 -->
    <div>等待的转移</div>
    <div class="transitions">
        <el-select v-model="flow_selected" class="m-2" placeholder="Select Me" size="large">
            <el-option v-for="flow_name in detail.ticket.valid_flow" :key="flow_name" :label="flow_name" :value="flow_name" />
        </el-select>
    </div>
    <hr/>
    <!-- 5. 提交按钮部分 -->
      <el-button type="primary" @click="onSubmit">提交表单</el-button>
  </el-form>
  </template>

<script setup>

import { reactive , ref, watch} from 'vue'
import Edit2 from '../components/Edit2.vue'
import StateForm from '../components/StateForm.vue';
import {useTicketStore} from '../stores/ticket'

const ticket = useTicketStore()

const flow_selected = ref(null)

const form = reactive({

})

const current_transition = ref(null)
current_transition
watch

const transition_value = ref(null)

watch(transition_value, ( newValue, oldValue ) => {
    oldValue
    console.log(newValue)
    for(var i=0;i<transitions.length;i++){
        console.log(i)
        if(newValue==transitions[i].caption){
            current_transition.value=transitions[i]
            break
        }
    }
  })

const detail = reactive({
  "ticket": {
    "id": 3,
    "title": "MyTicketFour",
    "meta": {
      "creator_id": 1,
      "creator_name": "aa",
      "edit_time": 1686446917,
      "create_time": 1686446900
    },
    "state": "A",
    "valid_flow": [
      "维修送审"
    ]
  },
  "state_names": [
    "A",
    "B",
    "C"
  ],
  "form_repr": {
    "A": {
      "name": "A",
      "active": true,
      "model": {
        "事由": "草不够了"
      },
      "fields": [
        {
          "type": "str",
          "name": "事由",
          "required": true
        }
      ]
    },
    "B": {
      "name": "B",
      "active": false,
      "model": {},
      "fields": [
        {
          "id": 1,
          "type": "str",
          "name": "审批意见",
          "required": true
        }
      ]
    },
    "C": {
      "name": "C",
      "active": true,
      "model": {
        "完成与否": true,
        "浇了多少水": "一棵树",
        "完成情况简述": "可以的"
      },
      "fields": [
        {
          "id": 1,
          "type": "check",
          "name": "完成与否",
          "required": true
        },
        {
          "id": 2,
          "type": "radio",
          "selections": [
            "一棵树",
            "两棵树"
          ],
          "name": "浇了多少水",
          "required": true
        },
        {
          "id": 3,
          "type": "str",
          "name": "完成情况简述",
          "required": false
        }
      ]
    }
  }
})

const sns = detail.state_names
const frp = detail.form_repr
const tkt = detail.ticket

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
    console.log(frp['C'])
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