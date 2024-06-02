interface meal {
  item: string
  number: number
}

interface Coupon {
  couponID: number
  meal: meal[]
  price: number
}

export { type Coupon, type meal }
