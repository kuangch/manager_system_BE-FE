/* ========================================
 *  company : Dilusense
 *   author : Kuangch
 *     date : 2018/11/20
 * ======================================== */
import Vue from 'vue'
import VueRouter from 'vue-router'

import About from './about'
import Home from './home'
import Per from './per'

const packageJson = require('../../../../package')
import ENV  from '../../../service/environment/env.config'

const routerList = [{
        path: `/${packageJson.name}/`,
        name: 'home',
        icon: 'el-icon-service',
        component: Home,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: `/${packageJson.name}/about`,
        name: 'about',
        icon: 'el-icon-bell',
        component: About,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: `/${packageJson.name}/per`,
        name: 'per',
        icon: 'el-icon-time',
        component: Per,
        meta: {
            requiresAuth: true
        }
    }]

Vue.use(VueRouter)
const router = new VueRouter({
    mode: 'history',
    // base: `${ENV.routerBase}`,
    routes: [
        {
          path: '/',
          redirect: `/${packageJson.name}/`
        },
        ...routerList
    ]
})

/**
 * 校验登录状态
 */
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!Vue.$login()) {
            window.location.href = '/'
        } else {
            next()
        }
    } else {
        next() // 确保一定要调用 next()
    }
})

export default router
export {
    routerList
}

