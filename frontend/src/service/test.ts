export default class TestService {
    static async testApi() {
      const response = await fetch('/test')
      console.log(response)
      return response.json()
    }
  }
  