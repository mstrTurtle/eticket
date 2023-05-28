import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// 给AXIOS加JWT部分

import axios from 'axios';

axios.interceptors.request.use(
  config => {
    // 添加Authorization header
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => Promise.reject(error)
);

// 启动VUE APP，并且用上Element Plus这个Hook。

createApp(App).use(router).use(ElementPlus).mount('#app')
