/* ========================================
 *  company : Dilusense
 *   author : Kuangch
 *     date : 2018/11/22
 * ======================================== */

let css = {
    loaderOptions: {
        // 给 sass-loader 传递选项
        sass: {
            // @/ 是 src/ 的别名
            // 全局变量
            data: `@import "@/common/default.theme.scss";`
        }
    }
}

module.exports = css