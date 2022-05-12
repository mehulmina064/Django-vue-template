<template>
  <div id="app">
    <img src="./assets/Logo.png" class="el-image__inner">
    <!-- <video data-v-63db6b3e="" width="100%" autoplay="autoplay" loop="loop" muted="muted"><source data-v-63db6b3e="" src="https://static.prodo.in/assets/videos/homepage-2.mp4" type="video/mp4"></video> -->
    <router-view/>
  </div>

</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
