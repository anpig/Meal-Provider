<template>
  <!-- component -->
  <div class="container mx-auto bg-white px-5">
    <div class="flex flex-col-reverse shadow-lg lg:flex-row">
      <!-- left section -->
      <div class="min-h-screen w-full shadow-lg lg:w-3/5">
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
            @click="changeCategorie('alarcarte')"
            class="mr-4 rounded-2xl bg-yellow-500 px-5 py-1 text-sm text-white hover:bg-transparent hover:text-indigo-600"
          >
            單點
          </button>
          <button
            @click="changeCategorie('combo')"
            class="mr-4 rounded-2xl bg-yellow-500 px-5 py-1 text-sm text-white hover:bg-transparent hover:text-indigo-600"
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
            class="flex h-32 flex-col justify-between rounded-md border border-gray-200 px-3 py-3"
            v-for="meal in meals"
          >
            <div>
              <div class="font-bold text-gray-800">{{ meal.name }}</div>
            </div>
            <div class="flex flex-row items-center justify-between">
              <span class="self-end text-lg font-bold text-yellow-500">${{ meal.price }}</span>
              <img
                src="https://source.unsplash.com/sc5sTPMrVfk/600x600"
                class="h-14 w-14 rounded-md object-cover"
                alt=""
              />
            </div>
          </div>
        </div>
        <!-- end products -->
      </div>
      <!-- end left section -->
      <!-- right section -->
      <div class="w-full lg:w-2/5">
        <!-- header -->
        <div class="mt-5 flex flex-row items-center justify-between px-5">
          <div class="text-xl font-bold">Current Order</div>
          <div class="font-semibold">
            <span
              style="cursor: pointer"
              @click="test()"
              class="rounded-md bg-red-100 px-4 py-2 font-semibold text-red-500 hover:bg-transparent"
              >Clear All</span
            >
          </div>
        </div>
        <!-- end header -->
        <!-- order list -->
        <div class="mt-5 h-2/5 overflow-y-auto px-5 py-4">
          <div class="mb-4 flex flex-row items-center justify-between" v-for="(meal, index) in userOrder">
            <div class="flex w-2/5 flex-row items-center">
              <img
                src="https://source.unsplash.com/4u_nRgiLW3M/600x600"
                class="h-10 w-10 rounded-md object-cover"
                alt="test"
              />
              <span class="ml-4 text-sm font-semibold">{{ meal.name }}</span>
            </div>
            <div class="flex w-32 justify-between">
              <span
                v-if="meal.number > 0"
                style="cursor: pointer"
                @click="decreaseNumber(index)"
                class="bg-white-300 rounded-md border border-red-400 px-3 py-1 hover:bg-gray-100"
                >-</span
              >
              <span
                v-else
                style="cursor: pointer"
                @click="decreaseNumber(index)"
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
              <span class="mx-4 font-semibold">{{ meal.number }}</span>
              <span
                style="cursor: pointer"
                @click="increaseNumber(index)"
                class="bg-white-300 rounded-md border border-green-600 px-3 py-1 hover:bg-gray-100"
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
                <span class="text-xs font-semibold uppercase">cashless credit</span>
                <span class="text-xl font-bold text-yellow-500">$32.50</span>
                <span class="text-xs text-gray-400">Available</span>
              </div>
              <div class="rounded-md bg-gray-300 px-4 py-3 font-bold text-gray-800">Cancel</div>
            </div>
          </div>
        </div>
        <!-- end cash -->
        <!-- button pay-->
        <div class="mt-5 px-5">
          <div
            style="cursor: pointer"
            @click="test()"
            class="rounded-md bg-yellow-500 px-4 py-4 text-center font-semibold text-white shadow-lg hover:bg-transparent hover:text-indigo-600"
          >
            Pay With Cashless Credit
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
import restaurantService from '@/service/restaurantService'
import type { restaurant } from '@/types/restaurant'
import { type meal } from '@/types/restaurant'
import { useUserStore } from '@/store/user'

const meals = ref<meal[]>([])
const categorie = ref('alarcarte')
const userStore = useUserStore()

const restaurantInfo = reactive<restaurant>({
  restaurant: '',
  meals: []
})

const userOrder = reactive<any[]>([])
const price = ref(0)

onMounted(async () => {
  await getRestaurant()
  meals.value = restaurantInfo.meals.filter((meal: any) => meal.type === 'alarcarte')
})
const getRestaurant = async () => {
  const data = await restaurantService.getRestaurant()
  restaurantInfo.restaurant = data.restaurant
  restaurantInfo.meals = data.meals
}

const changeCategorie = (type: string) => {
  categorie.value = type
  meals.value = restaurantInfo.meals.filter((meal: any) => meal.type === type)
}

const showName = (meal: meal) => {
  userOrder.push({ name: meal.name, number: 1, price: meal.price })
  price.value += meal.price
  alert(meal.name)
}

const test = () => {
  alert('test')
}

const decreaseNumber = (index: number) => {
  userOrder[index].number -= 1
  price.value -= userOrder[index].price
}

const increaseNumber = (index: number) => {
  userOrder[index].number += 1
  price.value += userOrder[index].price
}
</script>
