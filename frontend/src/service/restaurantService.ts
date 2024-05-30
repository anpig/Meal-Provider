import type { restaurant, order } from '../types/restaurant'

export default class restaurantService {
  static async getRestaurant(token: string): Promise<restaurant> {
    const response = await fetch('/api/pos/menu', {
      headers: {
        Authorization: 'Bearer ' + token
      }
    })
    const data = await response.json()
    const info = {
      restaurant: 'Fake Restaurant',
      meals: data.meals
    }
    return info
  }
  static async checkOuth(token: string): Promise<boolean> {
    const response = await fetch('/api/pos/get_order', {
      headers: {
        Authorization: 'Bearer ' + token
      }
    })
    console.log(response)
    if (response.status === 200) {
      return true
    } else {
      return false
    }
  }
  static async addOrder(token: string, order: order): Promise<void> {
    const response = await fetch('/api/pos/add_order', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(order)
    })
    return
  }
}
