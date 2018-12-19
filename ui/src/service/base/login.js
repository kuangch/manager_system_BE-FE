/* ========================================
 *  company : Dilusense
 *   author : Kuangch
 *     date : 2018/10/18
 * ======================================== */

export default function (Vue) {

    /**
     * 登录校验
     * @type {$login}
     */
    Vue.$login = Vue.prototype.$login = function () {

        let curr = new Date()

        let last = localStorage.getItem('time')

        if(last){
            if(curr.getTime() - last < 1000* 100){
                return true
            }
        }

        return false
    }
}
