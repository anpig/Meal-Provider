import type { restaurant } from '../types/restaurant'

export default class restaurantService {
  static async getRestaurant(token: string): Promise<restaurant> {
    const response = await fetch("/api/pos/menu", {
      headers: {
        "Authorization": "Bearer " + token
      }
    });
    const data = await response.json();
    console.log(data)
    return {
      restaurant: 'Fake Restaurant',
      meals: [
        {
          name: '單點一',
          type: 'alarcarte',
          price: 25,
          description: 'This is a fake meal'
        },
        {
          name: '單點二',
          type: 'alarcarte',
          price: 40,
          description: 'This is a fake meal'
        },
        {
          name: '單點三',
          type: 'alarcarte',
          price: 25,
          description: 'This is a fake meal'
        },
        {
          name: '套餐一',
          type: 'combo',
          price: 100,
          description: 'This is a fake meal'
        }
      ]
    }
  }
}
