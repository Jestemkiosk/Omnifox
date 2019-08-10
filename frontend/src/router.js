import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import CitiesView from './views/CitiesView.vue'
import FoxesView from './views/FoxesView.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/cities/',
      name: 'cities',
      component: CitiesView
    },
    {
      path: '/foxes/',
      name: 'foxes',
      component: FoxesView
    },
    {
      path: '/',
      name: 'home',
      component: Home
    }
  ]
})
