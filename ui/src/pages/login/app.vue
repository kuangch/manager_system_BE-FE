<template>
    <div>
        <el-button type="primary" class="dilu-button-main" @click="login">登录</el-button>
    </div>
</template>

<script>

const packageJson = require('../../../package')
export default {
    name: "login",
    methods: {
        login: function () {
            let curr = new Date()
            localStorage.setItem('time',curr.getTime())
            window.location.href = `/${packageJson.name}/`
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