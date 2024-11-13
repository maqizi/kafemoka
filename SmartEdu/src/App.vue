<template>
  <div id="app">
  <!-- 当前路由对应的组件将会渲染在这里 -->
  <router-view></router-view>
  <!-- <SignIn></SignIn> -->
  </div>
</template>

<script>
import SignIn from './components/SignIn.vue'
import Workspace from './components/workspace.vue'
export default {
  name: 'app',
  components: {
    SignIn,
    Workspace
  }
}
</script>

<style>
*{
	padding:0;
	margin: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
