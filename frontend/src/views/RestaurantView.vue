<template>
  <!-- component -->
  <div class="mx-auto bg-white px-5">
    <div class="flex flex-col-reverse lg:flex-row">
      <RestaurantSidebar class="w-full shadow-lg lg:w-1/6"></RestaurantSidebar>
      <!-- left section -->
      <div class="min-h-screen w-full bg-gray-100 lg:w-3/6">
        <!-- header -->
        <div class="mt-5 flex flex-row items-center justify-between px-5">
          <div class="text-gray-800">
            <div class="text-3xl font-bold">{{ restaurantInfo.restaurant }}</div>
          </div>
        </div>
        <!-- end header -->
        <!-- categories -->
        <div class="mt-5 flex flex-row px-5">
          <button
            @click="changeCategorie(false)"
            class="w-1/6 rounded-2xl bg-yellow-500 px-5 py-1 text-sm text-white hover:bg-transparent hover:text-indigo-600"
          >
            單點
          </button>

          <button
            @click="changeCategorie(true)"
            class="w-1/6 rounded-2xl border border-yellow-500 bg-transparent px-4 py-2 font-semibold text-yellow-500 hover:border-transparent hover:bg-yellow-500 hover:text-white"
          >
            套餐
          </button>
        </div>
        <!-- end categories -->
        <!-- products -->
        <div class="mt-5 grid h-3/4 grid-cols-3 gap-4 overflow-y-auto px-5">
          <div
            style="cursor: pointer"
            @click="showName(meal)"
            class="flex h-32 flex-col justify-between rounded-md border bg-white px-3 py-3"
            v-for="meal in meals"
          >
            <div>
              <div class="font-bold text-gray-800">{{ meal.name }}</div>
            </div>
            <div class="flex flex-row items-center justify-between">
              <span class="self-end text-lg font-bold text-yellow-500">${{ meal.price }}</span>
              <img :src="meal.picture" class="h-14 w-14 rounded-md object-cover" alt="" />
            </div>
          </div>
        </div>
        <!-- end products -->
      </div>
      <!-- end left section -->
      <!-- right section -->
      <div class="w-full shadow-lg lg:w-2/6">
        <!-- header -->
        <div class="mt-5 flex flex-row items-center justify-between px-5">
          <div class="text-xl font-bold">Current Order</div>
          <div class="font-semibold">
            <span
              style="cursor: pointer"
              @click="clearAllMeal()"
              class="rounded-md border border-red-500 bg-red-100 px-4 py-2 font-semibold text-red-500 hover:bg-transparent"
              >Clear All</span
            >
          </div>
        </div>
        <!-- end header -->
        <!-- order list -->
        <div class="mt-5 h-2/5 overflow-y-auto px-5 py-4">
          <div class="mb-4 flex flex-row items-center justify-between" v-for="(meal, index) in userOrder">
            <div class="flex w-2/5 flex-row items-center">
              <img :src="meal.picture" class="h-10 w-10 rounded-md object-cover" alt="test" />
              <span class="ml-4 text-sm font-semibold">{{ meal.name }}</span>
            </div>
            <div class="flex w-32 justify-between">
              <span
                v-if="meal.number > 0"
                style="cursor: pointer"
                @click="decreaseNumber(index)"
                class="bg-white-300 select-none rounded-md border border-red-400 px-3 py-1 hover:bg-gray-100"
                >-</span
              >
              <span
                v-else
                style="cursor: pointer"
                @click="deleteMeal(index)"
                class="bg-white-300 rounded-md border border-red-400 px-3 py-1 hover:bg-gray-100"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-6 w-2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"
                  />
                </svg>
              </span>
              <span class="select-none px-3 py-1 font-semibold">{{ meal.number }}</span>
              <span
                style="cursor: pointer"
                @click="increaseNumber(index)"
                class="bg-white-300 select-none rounded-md border border-green-600 px-3 py-1 hover:bg-gray-100"
                >+</span
              >
            </div>
            <div class="w-16 text-center text-lg font-semibold">${{ meal.price }}</div>
          </div>
          <!-- <div class="mb-4 flex flex-row items-center justify-between">
            <div class="flex w-2/5 flex-row items-center">
              <img
                src="https://source.unsplash.com/4u_nRgiLW3M/600x600"
                class="h-10 w-10 rounded-md object-cover"
                alt=""
              />
              <span class="ml-4 text-sm font-semibold">Ranch Burger</span>
            </div>
            <div class="flex w-32 justify-between">
              <span class="rounded-md bg-red-300 px-3 py-1 text-white">x</span>
              <span class="mx-4 font-semibold">1</span>
              <span class="rounded-md bg-gray-300 px-3 py-1">+</span>
            </div>
            <div class="w-16 text-center text-lg font-semibold">$2.50</div>
          </div> -->
        </div>
        <!-- end order list -->
        <!-- totalItems -->
        <div class="mt-5 px-5">
          <div class="rounded-md py-4 shadow-lg">
            <!-- <div class="flex justify-between px-4">
              <span class="text-sm font-semibold">Subtotal</span>
              <span class="font-bold">$35.25</span>
            </div>
            <div class="flex justify-between px-4">
              <span class="text-sm font-semibold">Discount</span>
              <span class="font-bold">- $5.00</span>
            </div> -->
            <div class="mt-3 flex items-center justify-between border-t-2 px-4 py-2">
              <span class="text-2xl font-semibold">Total</span>
              <span class="text-2xl font-bold" :value="price">${{ price }}</span>
            </div>
          </div>
        </div>
        <!-- end total -->
        <!-- cash -->
        <div class="mt-5 px-5">
          <div class="rounded-md px-4 py-4 shadow-lg">
            <div class="flex flex-row items-center justify-between">
              <div class="flex flex-col">
                <span class="text-xs font-semibold uppercase">Worker ID</span>
              </div>
              <input
                v-model="submitOrder.customer_id"
                class="w-3/4 rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900"
                placeholder="請輸入員工ID"
              />
            </div>
          </div>
        </div>
        <!-- end cash -->
        <!-- button pay-->
        <div class="mt-5 px-5">
          <div
            style="cursor: pointer"
            @click="submitUserOrder()"
            class="rounded-md bg-yellow-500 px-4 py-4 text-center font-semibold text-white shadow-lg hover:bg-transparent hover:text-indigo-600"
          >
            Submit Order
          </div>
        </div>
        <!-- end button pay -->
      </div>
      <!-- end right section -->
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed, reactive, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import restaurantService from '@/service/restaurantService'
import type { restaurant, meal, order } from '@/types/restaurant'
import { useUserStore } from '@/store/user'
import router from '@/router'

const meals = ref<meal[]>([])
const userStore = useUserStore()

const { userInfo } = storeToRefs(userStore)
const restaurantInfo = reactive<restaurant>({
  restaurant: '',
  meals: []
})

const userOrder = reactive<any[]>([])
const submitOrder = reactive<order>({
  customer_id: 100006,
  total_price: 0,
  dishes: []
})
const price = ref(0)

onMounted(async () => {
  const OuthResult = await restaurantService.checkOuth(userInfo.value.outh_token)
  if (OuthResult === false) {
    alert('請重新登入')
    router.push('/')
  }
  await getRestaurant()
  meals.value = restaurantInfo.meals.filter((meal: any) => meal.combo === false)
})
const getRestaurant = async () => {
  const data = await restaurantService.getRestaurant(userInfo.value.outh_token)
  restaurantInfo.restaurant = data.restaurant
  restaurantInfo.meals = data.meals
}

const changeCategorie = (type: boolean) => {
  meals.value = restaurantInfo.meals.filter((meal: any) => meal.combo === type)
}

const showName = (meal: meal) => {
  userOrder.push({ name: meal.name, number: 1, price: meal.price, dish_id: meal.dish_id })
  price.value += meal.price
  alert(meal.name)
}

const submitUserOrder = () => {
  submitOrder.total_price = price.value
  for (let i = 0; i < userOrder.length; i++) {
    submitOrder.dishes.push({
      dish_id: userOrder[i].dish_id,
      number: userOrder[i].number
    })
  }
  console.log(submitOrder)
  restaurantService.addOrder(userInfo.value.outh_token, submitOrder)
  submitOrder.dishes.splice(0, submitOrder.dishes.length)
  userOrder.splice(0, userOrder.length)
  price.value = 0
  
}

const decreaseNumber = (index: number) => {
  userOrder[index].number -= 1
  price.value -= userOrder[index].price
}

const increaseNumber = (index: number) => {
  userOrder[index].number += 1
  price.value += userOrder[index].price
}

const deleteMeal = (index: number) => {
  userOrder.splice(index, 1)
}

const clearAllMeal = () => {
  userOrder.splice(0, userOrder.length)
  price.value = 0
}
</script>
