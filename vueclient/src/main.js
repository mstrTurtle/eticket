import { createApp } from 'vue'
/*import './style.css'*/
import axios from "axios"
import App from './App.vue'
import './styles/index.scss'
import router from "./router"

const app=createApp(App)
app.use(router)
app.config.globalProperties.$axios=axios
app.mount('#app')
