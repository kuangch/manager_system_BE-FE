<template>
  <div>
    <el-button @click="getData">请求数据</el-button>
  </div>
</template>
<script>
    export default{
        name: 'about',
        methods: {
            getData: function(){
                this.axios.get('config').then(data=>{
                    this.$message.info(JSON.stringify(data.data));
                })
            }
        }
    }
</script>
<style lang="scss" scoped>
  div{
    color: $color_content_txt;
    font-size: 5vw;
  }
</style>