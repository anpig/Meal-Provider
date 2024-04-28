export default class CouponService {
  static async getAllCoupons() {
    const response = await fetch('/coupon')
    return response.json()
  }
}
