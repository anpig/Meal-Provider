import { defineStore } from 'pinia'
import type { Coupon, meal } from '@/types/coupon'

export const useCouponStore = defineStore({
  id: 'coupon',
  state: () => ({
    coupons: [] as Coupon[],
    charts: [] as meal[]
  }),
  actions: {
    addItem(item: meal) {
      this.charts.push(item)
    },
    removeItem(index: number) {
      this.charts.splice(index, 1)
    },
  }
})
