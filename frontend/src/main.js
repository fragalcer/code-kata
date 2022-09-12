import 'bootstrap/dist/css/bootstrap.min.css'
import Vue from 'vue'
import App from './App.vue'
import * as uiv from 'uiv'

Vue.config.productionTip = false

let vue = new Vue({
  render: h => h(App),
}).$mount('#app')

vue.use(uiv, {prefix: 'uiv'})
