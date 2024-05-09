import type {restaurant} from '../types/restaurant'

export default class restaurantService {
  static async getRestaurant(): Promise<restaurant> {
    return {
        restaurant: "Fake Restaurant",
        meals: [
            {
                name: "alarcarte1",
                type: "alarcarte",
                price: 25,
                description: "This is a fake meal",
            },
            {
                name: "alarcarte2",
                type: "alarcarte",
                price: 40,
                description: "This is a fake meal",
            },
            {
                name: "combo1",
                type: "combo",
                price: 100,
                description: "This is a fake meal",
            },
        ],
    }
  }
}
