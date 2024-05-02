import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import RestaurantView from '@/views/RestaurantView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: '/',
      component: HomeView
    },
    {
      path: '/restaurant',
      name: 'Restaurant',
      component: RestaurantView
    }
    // {
    //   path: '/worker',
    //   name: 'Worker',
    //   component: () => import('@/views/WorkerView.vue')
    // },
    // {
    //   path: 'admin',
    //   name: 'Admin',
    //   component: () => import('@/views/AdminView.vue')
    // }
  ]
})

export default router
