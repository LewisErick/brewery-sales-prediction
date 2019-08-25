import Vue from 'vue'
import VueGoogleCharts from 'vue-google-charts'
import Router from 'vue-router'
import Calendar from '@/components/Calendar'

Vue.use(VueGoogleCharts)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Calendar',
      component: Calendar
    }
  ]
})
