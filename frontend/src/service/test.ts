export default class TestService {
  static async testApi(): Promise<any> {
    const response = await fetch('/test')
    const result = await response.json()

    return result
  }
}
