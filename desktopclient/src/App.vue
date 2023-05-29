<template>
  <div id="app">
    <p>
      <router-link class="link" to="/">Home</router-link>
    <router-link class="link" to="/about">About</router-link>
    <router-link class="link" to="/login">Login</router-link>
    <router-link class="link" to="/allticket">AllTicket</router-link>
    <router-link class="link" :to="{ name: 'EditTicket', query: { id: 123 }}">EditTicket</router-link>
    <router-link class="link" :to="{ name: 'NewTicket'}">NewTicket</router-link>
    </p>
    <router-view></router-view>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'app',
  // components: {
  //   HelloWorld
  // }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  /* color: #2c3e50; */
  /* margin-top: 60px; */
}

.link{
  margin:3px;
  font-family:Verdana, Geneva, Tahoma, sans-serif
}
</style>
