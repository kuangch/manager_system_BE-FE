const  CompressionPlugin = require('compression-webpack-plugin')
const  UglifyJSPlugin = require('uglifyjs-webpack-plugin')

const devServer = require('./build/dev-server')
const css = require('./build/css-loader')
const settings = require('./config')

let config = {

    devServer,
    css,
    outputDir: settings.outputDir,

    // 链式配置
    chainWebpack:(config) =>{

        // config.resolve.alias
        //     .set('vue$', 'vue/dist/vue.js')

        config.devtool("source-map")

        // 小于3k的图片转成base64
        const imageRule = config.module.rule('images')
        // imageRule.uses.clear()
        imageRule.test(/.(png|jpe?g|gif)(\?\.*)?$/)
            .use('url-loader')
            .loader('url-loader')
            .tap(options => Object.assign({},options, {
                    limit: 1024 * 3,
                    name: 'img/[name].[hash:8].[ext]'
                })
            )


        // 代码分割
        const commonOptions = {
            chunks: 'all',
            reuseExistingChunk: true
        }
        config.optimization.splitChunks({
            // chunks: 'initial',
            // automaticNameDelimiter: '-',
            // name: true,
            cacheGroups: {
                dll: {
                    test: /[\\/]node_modules[\\/](vue|jquery)[\\/]/,
                    name: "chunk-vendors",
                    priority: 10,
                    ...commonOptions
                },

                // 这里定义的是在分离前被引用过2次以上的文件，将其一同打包到common.js中
                // common:{
                //     chunks: 'all',
                //     name: "common",
                //     minChunks: 2,
                //     minSize: 5
                // }
            }
        })

    },

    // 普通配置
    configureWebpack: config => {
        if (process.env.NODE_ENV === 'production') {
            // 为生产环境修改配置...
            return {
                plugins:[
                    new UglifyJSPlugin({
                        uglifyOptions: {
                            compress: {
                                warnings: false,
                                drop_debugger: true,
                                drop_console: true
                            }
                        }
                    }),
                    new CompressionPlugin({
                        test: /\.js$|\.html$|\.css/,
                        threshold:10240,
                        deleteOriginalAssets:false
                    })
                ]
            }

        } else {
            // 为开发环境修改配置...
        }
    },
}


// 多页应用配置
const glob = require('glob')
const path = require('path')
const packageJson = require('./package.json')
const PAGES_PATH = path.resolve(__dirname, './src/pages')
const pages = {}
const projectName = packageJson.name

const getHtmlFile = function (pageName) {
    let fileName = `${projectName}/${pageName}.html`
    switch (pageName){
        case 'main':
            fileName = `${projectName}/index.html`
            break
        case 'login':
            fileName = 'index.html'
            break
    }

    return fileName
}

glob.sync(PAGES_PATH + '/*/index.js').forEach(filepath => {
    let pageName = path.basename(path.dirname(filepath))
    pages[pageName] = {
        entry:filepath,
        title: pageName === 'main' ? projectName : pageName,
        filename: getHtmlFile(pageName),
        // chunks:['vue_jquery',pageName]
    }
})

config.pages = pages

module.exports = config