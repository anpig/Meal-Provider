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

interface order {
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

export { type restaurant, type meal, type order }
