<template>
    <div class="ext-large-title">工单详情页：{{ this.$route.query["id"] }}</div>
    <hr/>
    <!-- <Edit2></Edit2> -->
    <div class="meta-info">
            <div>id: {{ticket.id}}</div>
            <div>发起人: 小明</div>
            <div>当前: 小王</div>
    </div>
    <hr/>
    <el-steps :active="active" finish-status="success">
        <el-step v-for="block in ticket.blocks" :key="block.id" :title="'给'+block.people" />
    </el-steps>

    <el-form :model="form" label-width="120px">
    <!-- <el-form-item label="账号">
      <el-input v-model="form.name" placeholder="请输入账号" />
    </el-form-item>
    <el-form-item label="密码">
      <el-input v-model="form.password" type="password" placeholder="请输入密码" show-password />
    </el-form-item>
     -->
     <hr/>
    <div class="black-cicle" v-for="block in ticket.blocks" v-bind:key="block.id">
        <el-form-item v-for="field in block.fields" v-bind:key="field.id" :label="field.name">
            <div v-if="field.active">
                <div class="small-caption" v-if="field.type=='str'">
                    <el-input v-model="form[field.name]" :disabled="!block.active" :value="field.value"></el-input>
                </div>
                <div class="small-caption" v-else-if="field.type=='check'">
                    <el-checkbox v-model="form[field.name]" :disabled="!block.active" :checked="field.value"></el-checkbox>
                </div>
                <div class="small-caption" v-else-if="field.type=='radio'">
                    <el-radio-group v-model="form[field.name]">
                        <el-radio v-for="selection in field.selections" :key="selection" :label="selection" :disabled="!block.active">{{ selection }}</el-radio>
                    </el-radio-group>
                </div>
            </div>
            <div v-else>
                <div v-if="field.type=='str'">
                    <el-input v-model="field.value" :disabled="!block.active" :value="field.value"></el-input>
                </div>
                <div v-else-if="field.type=='check'">
                    <el-checkbox v-model="field.value" :disabled="!block.active" :checked="field.value"></el-checkbox>
                </div>
                <div v-else-if="field.type=='radio'">
                    <el-radio-group v-model="field.value">
                        <el-radio v-for="selection in field.selections" :key="selection" :label="selection" :disabled="!block.active">{{ selection }}</el-radio>
                    </el-radio-group>
                </div>
            </div>
           
        </el-form-item>
        <div class="noting">{{block.active?"当前填写位置":""}}</div>
    </div>
    <hr/>
    <div class="transitions">
        <el-select v-model="transition_value" class="m-2" placeholder="Select" size="large">
            <el-option
            v-for="transition in transitions"
            :key="transition.caption"
            :label="transition.caption"
            :value="transition.caption"
            />
        </el-select>
        <div>
            <div v-if="!current_transition">
                请选择
            </div>
            <div v-else-if="current_transition.fields.length==0">
                无需填写字段
            </div>
            <div v-else>
            <div>等待填入的参数:</div>
            <el-form-item v-for="field in current_transition.fields" v-bind:key="field.id" :label="field.name">

                    <div v-if="field.type=='str'">
                        <el-input v-model="form[field.name]"  :value="field.value"></el-input>
                    </div>
                    <div v-else-if="field.type=='check'">
                        <el-checkbox v-model="form[field.name]"  :checked="field.value"></el-checkbox>
                    </div>
                    <div v-else-if="field.type=='radio'">
                        <el-radio-group v-model="form[field.name]">
                            <el-radio v-for="selection in field.selections" :key="selection" :label="selection">{{ selection }}</el-radio>
                        </el-radio-group>
                    </div>
               
            
            </el-form-item>
            </div>
        </div>
    </div>
    
    <el-form-item>
      <el-button type="primary" @click="onSubmit">提交表单</el-button>
    </el-form-item>
  </el-form>
  </template>

<script setup>

import { reactive , ref, watch} from 'vue'
import Edit2 from '../components/Edit2.vue'


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

const ticket = reactive({
    id:12355,
    title:'花要萎了需要浇花',
    blocks:[
        {
            id:1,
            people:"后勤部小张",
            active:false,
            fields:[{
                type:"str",
                name:"事由",
                required: true,
                value:"花要死了"
            }]
        },
        {
            id:2,
            people:"赵局长",
            active:true,
            fields:[{
                id:1,
                type:"str",
                name:"审批意见",
                required: true,
                value:"重新写"
            }]
        },
        {
            id:3,
            people:"园丁小王",
            active:false,
            fields:[{
                id:1,
                type:"check",
                name:"完成与否",
                required: true,
                value:false
            },
            {
                id:2,
                type:"radio",
                selections:["一棵树","两棵树"],
                name:"浇了多少水",
                required: true,
                value:"一棵树"
            },
            {
                id:3,
                type:"str",
                name:"完成情况简述",
                required: false,
                value:"大中午根本浇不了水，一浇水等着烧苗吧。"
            }]
        }
    ]
})

const transitions = reactive([
    {
        id:1,
        caption:"直接驳回",
        program:"reject",
        fields:[]
    },
    {
        id:2,
        caption:"送下去执行",
        fields:[{
                id:1,
                type:"str",
                name:"交给谁",
                required: true,
                value:""
        }]
    }
])

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
}


// do not use same name with ref
// const form = reactive({
//   name: '',
//   password: ''
// })
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
    border:1px solid red;
    border-radius:5px;
    padding:4px;
    text-align: center;
    margin:5px;
}
.black-cicle{
    border:2px solid black;
    border-radius:5px;
    padding:4px;
    text-align: center;
    margin:5px;
}

</style>