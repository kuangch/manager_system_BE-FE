/* ========================================
 *  company : Dilusense
 *   author : Kuangch
 *     date : 2018/7/20
 * ======================================== */

let urlPrefix = '/dev_test'

let vars = {}
switch (process.env.NODE_ENV) {
    case 'development':
        vars.baseUrl = urlPrefix  //这里是本地的请求url
        vars.routerBase = '/app/'
        break
    case 'production':
        vars.baseUrl = "/"   //生产环境url
        vars.routerBase = "/"
        break
}

export default {
    ...vars
}