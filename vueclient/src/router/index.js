import {createRouter,createWebHashHistory} from "vue-router"
import AppLayout from "../components/layout/AppLayout.vue"
import loginview from "../views/Login.vue"
import IndexView from "../views/indexview.vue"
import TicketsView from "../views/TicketShow.vue"
import TicketEditView from "../views/TicktetEdit.vue"


const routes = [
    {
        path:"/",
        name:"home",
        component:AppLayout,    
        meta: {RequestsAuth:true},
        children:[{
            path:"",
            component:IndexView,
        },{
            path:"/show",
            name:"show",
            component:TicketsView,
        },{
            path:"/edit",
            name:"edit",
            component:TicketEditView,
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

router.beforeEach((to,from,next)=>{
    // if (to.matched.some(r=>r.meta?.RequestsAuth)){

    // }
    // next()
  if (to.path === '/login') return next()
  const tokenStr = window.sessionStorage.getItem('token')
  // 没有token， 强制转到login页面
  if (!tokenStr) return next('/login')
  next()
})

export default router;