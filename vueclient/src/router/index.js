import {createRouter,createWebHashHistory} from "vue-router"
import AppLayout from "../components/layout/AppLayout.vue"
import loginview from "../components/Login.vue"
import IndexView from "../components/HelloWorld.vue"

const routes = [
    {
        path:"/",
        name:"home",
        component:AppLayout,    
        children:[{
            path:"",
            component:IndexView,
        }]
    },
    {
        path:"/login",
        name:"login",
        component:loginview,    
    }
]

const router =createRouter({
    history:createWebHashHistory(),
    routes
})

export default router;