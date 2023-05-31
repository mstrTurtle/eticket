// import axios from 'axios'

// /**
//  * 请求拦截
//  */
// axios.interceptors.request.use(
//     config => {
//         console.log('tokening');
//         const token = localStorage.getItem('token');
//         if (token) {
//             config.headers.Authorization = `Bearer ${token}`;
//         }else {
//             console.log('no token');
//         }
//         return config;
//     },
//     error => {
//         console.log('error in request');
//         return Promise.reject(error);
//     }
// );



// // 导出给 main.js 挂载
// export default axios;
