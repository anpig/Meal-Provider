interface meal {
  dish_id: number
  name: string
  description: string
  combo: boolean
  price: number
  rating: number
  order_times: number
  picture: string
  available: number
}

interface chart {
  customer_id: number
  total_price: number
  dishes: {
    dish_id: number
    number: number
  }[]
}

interface restaurant {
  restaurant: string
  meals: meal[]
}

interface order {
  order_id: number
  order_time: string
  restaurant_id: number
  total_price: number
  finished: boolean
  reviewed: number
  overall_rating: number
  dishes: {
    dish_id: number
    dish_name: string
    number: number
    price: number
    rating: number
  }[]
}

export { type restaurant, type meal, type chart, type order }
