import { createApp } from 'vue'
/*import './style.css'*/

import App from './App.vue'
import './styles/index.scss'
import router from "./router"

import axios from 'axios';

// axios.interceptors.request.use(
//     config => {
//       config.headers.token='xxx';
//       // 添加Authorization header
//       const token = localStorage.getItem('token');
//       console.log("111")
//       if (token) {
//         config.headers['Authorize'] =  `Bearer ${token}`;
//       }
//       return config;
//     },
//     error => Promise.reject(error)
//   );

const app=createApp(App)
app.use(router)
app.config.globalProperties.$axios=axios
app.mount('#app')
