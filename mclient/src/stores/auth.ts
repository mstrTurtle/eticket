// @ts-check
import { defineStore, acceptHMRUpdate } from 'pinia'
import axios from 'axios'
import {useRouter} from 'vue-router'


interface LoginData {
    // name: string;
    id: number;
    token: string;
}

interface Statics {
    // name: string;
    day_done: number;
    day_total: number;
    week_done: number;
    week_total: number;
    overdue_cnt: number;
    total: number;
}

interface MeData {
    // name: string;
    name: string;
    groups: [string];
}

interface Workflow {
    id: number;
    name: string;
    groups: string[]; // 哪些group可发起
    fields: Record<string, Object>;
}

interface UserData {
    id: number;
    name: string;
    groups: [string];
}

type Noti = string[]


export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    name: '游客',
    isAdmin: true,
    instance : axios.create({
        baseURL: 'http://127.0.0.1:8000'
    }),
    notis:["No"],
    groups:[],
    loading:false,
    modal:false,
    info:"no info currently",
    token: null,
    workflows: null,
    statics: null  as Statics|null,
  }),

  actions: {
    logout() {
        this.$patch({
        token: null,
        name: '未登录',
        isAdmin: false,
        })
        // axios.defaults.headers.common['Authorization'] = null

      // we could do other stuff like redirecting the user
    },

    /**
     * Attempt to login a user
     */
    login(id: number, password: string) {
        this.$patch({
            loading: true,
            modal:false
        })
        this.instance.post('/api/login',null,{params:{id,password}})
        .then(resp=>{
            const userData = resp.data as LoginData
            console.log(userData)
            this.$patch({
                token: userData.token,
                loading: false,
                modal:false
                })
            // axios.defaults.headers.common['Authorization'] = "Bearer " + userData.token;
            
        })
        .catch((err)=>{
            console.log(err.message)
            this.$patch({
                loading: false,
                modal:true,
                info:"失败了：" + err.message
                })
        })

    },
    getMe() {
        // this.instance.get('/users/me',{headers:{Authorization:'Bearer '+ this.token}})
        this.instance.get('/users/me',{headers:{Authorization:`Bearer ${this.token}`}})
        .then((resp)=>{
            const meData = resp.data as MeData
            this.$patch({
                name: meData.name,
                groups: meData.groups
                })
        })
        .catch((err)=>{
            this.$patch({
                loading: false,
                modal:true,
                info:"失败了：" + err.message
                })
        })
    },
    getWorkflows(){
        this.instance.get(`/workflows`)
        .then((resp)=>{
            const workflows = resp.data as Workflow[]
            this.$patch({
                workflows
            })
        })
        .catch((err)=>{
            this.$patch({
                loading: false,
                modal:true,
                info:"失败了获取它"
            })
        })
    },
    getStatics(){
        this.instance.get(`/statics`)
        .then((resp)=>{
            const statics = resp.data as Statics
            this.$patch({
                statics
            })
        })
        .catch((err)=>{
            this.$patch({
                loading: false,
                modal:true,
                info:"失败了获取statics"
            })
        })
    },
    newTicket(workflow_id,title){
        this.instance.post('/tickets',{workflow_id,title},{headers:{Authorization:`Bearer ${this.token}`}})
    },
    /**
     * Attempt to fetch notifications
     */
    async getnoti() {
        this.instance.get('/notifications')
        .then(resp=>{
            const notis : Noti = resp.data
            this.$patch({
                notis:notis,
                })
        })
        .catch((err)=>{
            console.log(err.message)
            this.$patch({
                notis:["oh fuck 加载失败了"],
            })
        })
    },
  },
})
