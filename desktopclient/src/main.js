import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import './assets/css/main.css';

// 给AXIOS加JWT部分

// 启动VUE APP，并且用上Element Plus这个Hook。

createApp(App).use(router).use(ElementPlus).mount('#app')
