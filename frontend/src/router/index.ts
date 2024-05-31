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
    },
    {
      path: '/worker',
      name: 'Worker',
      component: () => import('@/views/worker/WorkerView.vue')
    },
    {
      path: '/history-order',
      name: 'History Order',
      component: () => import('@/views/worker/HistoryOrderView.vue')
    },
    {
      path: '/worker/restaurant/:id',
      name: 'WorkerRestaurant',
      component: () => import('@/views/worker/WorkerRestaurantView.vue')
    }
  ]
})

export default router
