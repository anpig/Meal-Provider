import type { order, restaurant } from '../types/worker'

export default class workerService {
  static async getRestaurantList(token: string): Promise<any[]> {
    const response = await fetch('/api/main/restaurant_list')
    const data = await response.json()
    return data.restaurants
  }

  static async getRestaurant(token: string, restaurant_id: string): Promise<restaurant> {
    const response = await fetch('/api/main/restaurant/' + restaurant_id, {
      headers: {
        Authorization: 'Bearer ' + token
      }
    })
    const data = await response.json()
    console.log(data)
    return data
  }

  static async getHistoryOrder(token: string): Promise<order[]> {
    const response = await fetch('/api/main/history', {
      headers: {
        Authorization: 'Bearer ' + token
      }
    })
    const data = await response.json()
    return data.orders
  }
}
