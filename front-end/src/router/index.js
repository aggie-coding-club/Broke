import { createRouter, createWebHistory } from 'vue-router'
import UserInputView from '../views/UserInputView.vue'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/result',
      name: 'result',
      component: () => import('../views/ResultView.vue')
    },
    {
      path: '/userinput',
      name: 'userinput',
      component: UserInputView
    }
  ]
})

export default router
