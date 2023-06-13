// @ts-check
import { defineStore, acceptHMRUpdate } from 'pinia'
import axios, { Axios ,AxiosInstance} from 'axios'
import { useAuthStore } from './auth';


// 获取所有工单

type AllTicket = TicketBrief[]

interface TicketBrief {
    id: number;
    title: string;
    created_time: number; // UNIX时间戳
    created_user_name: string;
}

// 获取某工单详情

interface TicketDetail{
    id: number;
    title: string;
    form_model: string;
    ticket_type: TicketType
}

// 发起新工单

interface NewTicket{
    ticket_type_id: number;
    title: string;
}

// 编辑工单

interface EditTicket {
    id: number;
    flow_name: string;
    model: string;
}

interface Model {
    // 这里可以定义模型对象的属性和类型，具体根据实际需求来定义
}

// 工单类型

interface TicketType {
    id: number;
    name: string;
    groups: string[]; // 哪些group可发起
    fields: Record<string, Field[]>;
}

interface Field {
    // 这里可以定义字段对象的属性和类型，具体根据实际需求来定义
}


const auth = useAuthStore()

export const useTicketStore = defineStore({
    id: 'ticket',
    state: () => ({
        detail: null,
        types:null,
        briefs:null,
        loading: false,
        modal: false,
        info: "暂时没有异常",
    }),

    actions: {
        setLoadingModal(){
            this.$patch({
                loading: true,
                modal:false,
                info:""
            })
        },
        resetLoadingModal(){
            this.$patch({
                loading: false,
                modal:false,
                info:""
            })
        },
        getTicketDetail(ticket_id:number){
            console.log('getTicketDetail')

            this.$patch({
                loading: true,
                modal:false
            })


            const inst:AxiosInstance = auth.$state.instance
            inst.get(`/tickets/${encodeURIComponent(ticket_id)}`)
            .then((resp)=>{
                const detail = resp.data as TicketDetail
                console.log(detail)
                this.$patch({
                    detail,
                    loading: false,
                    modal:false
                })
            })
            .catch((err)=>{
                this.$patch({
                    loading: false,
                    modal:true,
                    info:"失败了获取它: " + err.message
                })
            })
        },
        getAllTicket(){
            const inst:AxiosInstance = auth.$state.instance
            inst.get(`/tickets/`)
            .then((resp)=>{
                const briefs = resp.data as TicketBrief[]
                this.$patch({
                    briefs,
                    loading: false,
                    modal:false
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
        getTicketTypes(){
            const inst:AxiosInstance = auth.$state.instance
            inst.get(`/ticket_types`)
            .then((resp)=>{
                const types = resp.data as TicketType[]
                this.$patch({
                    types
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
        createTicket(nt:NewTicket){
            const inst:AxiosInstance = auth.$state.instance
            inst.post(`/tickets/`, nt)
            .then((resp)=>{
                this.$patch({
                    loading: false,
                    modal:true,
                    info:"成功了"
                })
            })
            .catch((err)=>{
                this.$patch({
                    loading: false,
                    modal:true,
                    info:"创建失败了"
                })
            })
        },
        async editTicket(flow_name, router){
            const et  = { id: this.detail.ticket.id, 
                          flow_name,
                          model: (this.detail.form_repr[this.detail.ticket.state].model)
                          } as EditTicket
            const inst:AxiosInstance = auth.$state.instance
            inst.post(`/tickets/${et.id}`, et)
            .then((resp)=>{
                this.$patch({
                    loading: false,
                    modal:true,
                    info:"成功了"
                })
                
                router.push({name:'AllTicket'})
            })
            .catch((err)=>{
                this.$patch({
                    loading: false,
                    modal:true,
                    info:"创建失败了"
                })
            })
        },
    }
})