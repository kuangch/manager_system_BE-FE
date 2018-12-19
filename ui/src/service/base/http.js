/* ========================================
 *  company : Dilusense
 *   author : Kuangch
 *     date : 2018/10/18
 * ======================================== */

import axios from 'axios'
import vueAxios from 'vue-axios'
import Vue from 'vue'
import ENV from '../environment/env.config'

axios.defaults.baseURL = ENV.baseUrl
axios.defaults.timeout = 1000 * 10

// 响应拦截（配置请求回来的信息）
axios.interceptors.response.use(function (response) {
    return response;
}, function (error) {
    // 处理响应失败
    if (error.response.status === 401) {
        console.warn('未登录,或者登录失效')
        // 未授权跳转到登录页
        window.location.href = '/'
    } else {
        return Promise.reject(error);
    }
});

export default function (Vue) {
    Vue.use(vueAxios,axios)
}
