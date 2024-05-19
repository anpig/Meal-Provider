import type { user } from '../types/user'

export default class userLoginService {
  static async userLogin(user_account: string, user_password: string): Promise<user> {
    console.log(user_account, user_password)
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ user_account: user_account, user_password: user_password })
    })
    const result = await response.json()
    return result
  }
}
