import type { restaurant } from '../types/restaurant'

export default class restaurantService {
  static async getRestaurant(token: string): Promise<restaurant> {
    const response = await fetch("/api/pos/menu", {
      headers: {
        "Authorization": "Bearer " + token
      }
    });
    const data = await response.json();
    const info = {
      restaurant: 'Fake Restaurant',
      meals: data.meals 
    }
    return info;
  }
}
