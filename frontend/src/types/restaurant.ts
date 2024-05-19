interface meal {
  name: string
  type: string
  price: number
  description: string
}

interface restaurant {
  restaurant: string
  meals: meal[]
}

export { type restaurant, type meal }
