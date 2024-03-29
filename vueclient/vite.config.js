import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Icons from 'unplugin-icons/vite'
import IconsResolver from 'unplugin-icons/resolver'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [ 
    AutoImport({
    resolvers: [
      ElementPlusResolver(),
      IconsResolver({
        prefix: 'Icon',
      }),
    ],
  }),
  Components({
    resolvers: [  
      IconsResolver({
        enabledCollections: ['ep'],
      }),
      ElementPlusResolver()],
  }),
  Icons({
    autoInstall: true,
  }),
  vue(),
 ],  
 transpileDependencies: true,
 
 server:{
  host:'0.0.0.0' ,//ip地址
  port: 8081, // 设置服务启动端口号
  open: true, // 设置服务启动时是否自动打开浏览器
}
})




