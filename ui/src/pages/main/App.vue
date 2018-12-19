<template>
  <div id="app">
    <header>
      <img src="../../assets/logo.png"/>
      <span class="app-name">配合式终端设备</span>
      <div class="right">
        <span><i class="el-icon-date"></i> {{user_info.privilege}}/{{user_info.name}}</span>
       <nav class="nav">
        <ul>
          <li @click="goHome"><a class="dilu-button-main btn-big" href="#">home</a></li>
          <li @click="goAbout"><a class="dilu-button-warn btn-big" href="#">about</a></li>
        </ul>
       </nav>
      </div>
    </header>
    <div class="main">
      <div class="nav">
        <router-link v-for="item in routerList" :key="item.name" :class="$route.path===item.path||$route.path.indexOf((item.path+'/'))===0?'app-router-link-active ovfl-ellipsis': 'ovfl-ellipsis'" :to="{path: `${item.path}`}"><i :class="item.icon"></i><span>{{item.name}}</span></router-link>
      </div>

      <div class="content">
        <router-view class="view"></router-view>
      </div>
    </div>

  </div>
</template>

<script>

const packageJson = require('../../../package')
import {routerList} from './router'

export default {
  name: 'app',
  mounted: function(){
  } ,
  data(){
      return {
          user_info:{
              name:'kuangch',
              privilege:'admin'
          },
          packageJson,
          routerList
      }
  },
  methods: {
     goHome: function () {
         window.open( 'home.html')
     },
     goAbout: function () {
         window.open( 'about.html')
     }
  }
}

</script>

<style lang="scss" scoped>
  $nav_max_w: 15vw;
  $header_content_height:2.3rem;

  #app{
    display: flex;
    min-height: 100vh;
    flex-direction: column;

  header{
    flex-basis: 4rem;
    background: $color_main;
    display: flex;
    justify-content: flex-start;
    align-items: center;

    color: $color_main_txt;

    img{
      margin-left: .8vw;
      height: $header_content_height + 0.3;
    }
    .app-name{
      margin-left: 1vw;
      font-size: calc(1rem + 6px);
      font-weight: bold;
    }

    .right{
      flex-grow: 1;//这三个元素只有它在有空余空间时可伸缩，也就是它占据了所有剩余空间
      display: flex;//将它设置为flex,就可以单独对他进行主轴右对齐
      justify-content: flex-end;

      span{
        font-size: calc(1rem + 2px);
        height: $header_content_height;
        line-height: $header_content_height;
        margin-right: 1vw;
        word-break: break-all;
      }
    }
    .nav{
      height: $header_content_height;
      line-height: $header_content_height;
      margin-right: .5vw;
    }
    .nav li{
      line-height: 100%;
      margin: 0 .5vw 0 0;
      padding: 0;
      list-style: none;
      display: inline-block;

    }
    @media (max-width: 720px){
      $item_w : 80px;
      .nav {
        width: $item_w;
        background: transparent;
        padding: 0 0;
      }

      .nav ul{
        position: absolute;
        z-index: 2;
      }
      .nav li {
        transition: opacity 500ms;
        opacity: 0; /* hide all <li> items */
        margin: 0;
      }
      .nav li:first-child {
        opacity:1;
      }
      .nav li a {
        display: block;
        border-radius: 0;
      }

      .nav:hover li {
        opacity:1;
      }
    }
  }
  >.main{
    display: flex;
    flex: 1;

    .nav{
      background: $color_content;
      border-right: solid 1px $color_division_line;
      flex: 0 0 $nav_max_w;
      max-width: $nav_max_w;

      $nav_item_height : 50px;
      a{
        padding-left: 2vw;
        display: block;
        text-decoration: none;
        color:$color_content_txt;
        background: white;
        height: $nav_item_height;
        line-height: $nav_item_height;
        transition: font-size 300ms;
        font-size: calc(1rem + 2px);

        i{
          margin-right: 0.5vw;
        }
      }
      a:hover{
        background: $color_main_second;
        color: white;
        font-size: 1.5rem;
        i{
          font-size: 1.5rem;
        }
      }
      .router-link-exact-active{
        background: $color_main_second;
        color: white;
      }

      @media (max-width: 720px){
        a{
          padding-left: 0;
          text-align: center;
          i{
            margin-right: 0;
            font-size: calc(1rem + 2px);
          }
          span{
            display: none;
          }
        }
      }
    }
    >.content{
      flex: 1;
      background: white;
      display: flex;
      align-items: center;
      justify-content: center;
    }
   }
  }

</style>
