<template>
    <div>
        <el-button type="primary" class="dilu-button-main" @click="login">登录</el-button>
    </div>
</template>

<script>

const packageJson = require('../../../package')
export default {
    name: "login",
    mounted(){
        let search = window.location.search
        if(search && search.substr(1).match(/redirect=true/)){
            this.$message.warning('未登录或登录失效，请重新登录')
        }

    },
    methods: {
        login: function () {
            this.axios.get('login').then(data=>{
                console.log(data)
                if(data.data.code === 0){
                    window.location.href = `/${packageJson.name}/`
                }
            }).catch(()=>{
                this.$message.info('登陆失败');
            })

        }
    }
}
</script>

<style scoped lang="scss">
    div{
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>