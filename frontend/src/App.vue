<template>
  <div id="app" class="container">
<!--    <img alt="Vue logo" src="./assets/logo.png">-->
    <BusinessLoanApp msg="Welcome to the Business Loans App!"/>
  </div>
</template>

<script>
import BusinessLoanApp from './components/BusinessLoanApp.vue'

export default {
  name: 'App',
  components: {
    BusinessLoanApp
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
