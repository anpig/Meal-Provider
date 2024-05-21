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

interface restaurant {
  restaurant: string
  meals: meal[]
}

export { type restaurant, type meal }
