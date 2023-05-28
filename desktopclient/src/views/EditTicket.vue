<template>
    <div class="ext-large-title">现在在编辑id为“{{ this.$route.query["id"] }}”的工单页</div>
    <div>
            <div>id: {{ticket.id}}</div>
            <div>title: {{ticket.title}}</div>
    </div>
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
    <div v-for="block in ticket.blocks" v-bind:key="block.id">
        <div class="small-caption">这是给“{{block.people}}”填写的(你{{block.active?"能":"不能"}}填)</div>
        <el-form-item v-for="field in block.fields" v-bind:key="field.id" :label="field.name">
            <div v-if="field.active">
                <div v-if="field.type=='str'">
                    <el-input v-model="form[field.name]" :disabled="!block.active" :value="field.value"></el-input>
                </div>
                <div v-else-if="field.type=='check'">
                    <el-checkbox v-model="form[field.name]" :disabled="!block.active" :checked="field.value"></el-checkbox>
                </div>
                <div v-else-if="field.type=='radio'">
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
    </div>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">提交表单</el-button>
    </el-form-item>
  </el-form>
  </template>

<script setup>

import { reactive , ref} from 'vue'

const form = reactive({

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
.ext-large-title{
    font-size:2lvw
    
}
.small-caption{
    text-align: left;
    color:red;
}
</style>