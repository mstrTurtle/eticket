// @ts-check
import { defineStore, acceptHMRUpdate } from 'pinia'
import axios from 'axios'

interface LoginData {
    // name: string;
    id: number;
    token: string;
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
  }),

  actions: {
    logout() {
        this.$patch({
        name: '',
        isAdmin: false,
        })

      // we could do other stuff like redirecting the user
    },

    /**
     * Attempt to login a user
     */
    login(id: number, password: string) {
        this.instance.post('/login')
        .then(resp=>{
            const userData = resp.data as LoginData
            this.$patch({
                token: userData.token,
                })
            
        })
        .catch((err)=>{
            console.log(err.message)
        })

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
