// import Vue from 'vue'
// import Vuex from 'vuex'
import { createApp } from 'vue'
import App from './App.vue'
import { router } from './router';
// import BootstrapVue from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// Vue.use(BootstrapVue)
// import {store} from '/router/store'

// Vue.config.productionTip=false
// Vue.use(Vuex)

// export const store=new Vuex.Store({
//     state:{
//         postlist: []
//     }
// })
createApp(App).use(router).mount('#app')
// const app=createApp(App);

// new Vue({
//   render: h => h(App),
//   router,
// }).$mount('#app')
// new Vue({
//     el: '#app',
//     render: h => h(App),
// })



// import { createApp, h } from 'vue'
// import App from './App.vnoue'
// // import VueRouter from 'vue-router'
// import BoardList from './components/BoardList'
// import BoardForm from './components/BoardForm'
// // import Home from './components/Home'
// import Error from './components/Error'
// import router from './router'

// // const app=createApp(App);
// // app.useAttrs(router);



// // const routes = [
// //   { path: '/board1', component: BoardList },
// //   { path: '/board2', component: BoardForm }
// // ]

// // const NotFoundComponent = { template: '<p>Page not found</p>' }
// // const HomeComponent = { template: '<p>Home page</p>' }
// // const AboutComponent = { template: '<p>About page</p>' }

// const routes = {
//   '/': App,
//   '/board1': BoardList,
//   '/board2': BoardForm,
//   '/error': Error
  
// }

// const SimpleRouter = {
//   data: () => ({
//     currentRoute: window.location.pathname
//   }),

//   computed: {
//     CurrentComponent() {
//       return routes[this.currentRoute] || Error
//     }
//   },

//   render() {
//     return h(this.CurrentComponent)
//   }
// }

// createApp(SimpleRouter).mount('#app')