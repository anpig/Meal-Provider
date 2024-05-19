import { defineStore } from 'pinia'
import { type user } from '@/types/user'

export const useUserStore = defineStore({
  id: 'userInfomation',
  state: () => ({
    userInfo: {
      outh_token: '',
      user_identity: ''
    } as user
  }),
  actions: {
    setUserInfo(user: user) {
      this.userInfo = user
      console.log(user)
    }
  }
})
