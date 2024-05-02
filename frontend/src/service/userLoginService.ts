import type { user } from '../types/user';

export default class userLoginService {
  static async userLogin(user_name: string, user_password: string): Promise<user> {
    // const response = await fetch('/login', {
    //   method: 'POST',
    //   headers: {
    //       'Content-Type': 'application/json'
    //   },
    //   body: JSON.stringify({ user_account, user_password })
    // });
    // const result = await response.json();
    return {
      outh_token: '123456',
      user_identity: 'invalid'
    }
  }
}
  