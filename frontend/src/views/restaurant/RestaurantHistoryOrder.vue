<template>
  <!-- component -->
  <!-- <successDialog restaurant"showDialog" @close="close()" message="Yo have success submit the order"></successDialog> -->
  <div class="mx-auto bg-white">
    <!-- component -->
    <div class="flex flex-col-reverse lg:flex-row">
      <RestaurantSidebar class="min-h-screen w-full justify-start shadow-lg lg:w-1/6"></RestaurantSidebar>

      <div class="w-full lg:w-5/6">
        <div class="px-4 py-4 md:px-10 md:py-7">
          <div class="flex items-center justify-between">
            <p
              tabindex="0"
              class="text-base font-bold leading-normal text-gray-800 focus:outline-none sm:text-lg md:text-xl lg:text-2xl"
            >
              訂單狀況
            </p>
          </div>
        </div>
        <div class="bg-white px-4 py-4 md:px-8 md:py-7 xl:px-10">
          <div class="items-center justify-between sm:flex">
            <div class="flex items-center">
              <a
                class="rounded-full focus:bg-indigo-50 focus:outline-none focus:ring-2 focus:ring-indigo-800"
                href=" javascript:void(0)"
              >
                <div class="rounded-full bg-indigo-100 px-8 py-2 text-indigo-700">
                  <p>All</p>
                </div>
              </a>
              <a
                class="ml-4 rounded-full focus:bg-indigo-50 focus:outline-none focus:ring-2 focus:ring-indigo-800 sm:ml-8"
                href="javascript:void(0)"
              >
                <div class="rounded-full px-8 py-2 text-gray-600 hover:bg-indigo-100 hover:text-indigo-700">
                  <p>Done</p>
                </div>
              </a>
              <a
                class="ml-4 rounded-full focus:bg-indigo-50 focus:outline-none focus:ring-2 focus:ring-indigo-800 sm:ml-8"
                href="javascript:void(0)"
              >
                <div class="rounded-full px-8 py-2 text-gray-600 hover:bg-indigo-100 hover:text-indigo-700">
                  <p>Pending</p>
                </div>
              </a>
            </div>
          </div>
          <div class="mt-7 overflow-x-auto">
            <table class="w-full whitespace-nowrap">
              <tbody>
                <tr class="h-16 rounded border border-gray-100 focus:outline-none">
                  <td>
                    <div class="ml-5"></div>
                  </td>
                  <td class="">
                    <div class="flex items-center pl-5">訂單時間</div>
                  </td>
                  <td class="pl-24"></td>
                  <td class="pl-5"></td>
                  <td class="pl-5"></td>
                  <td class="pl-0">
                    <div class="flex items-center">
                      <p class="ml-2 text-sm leading-none text-gray-600">員工ID</p>
                    </div>
                  </td>
                  <td class="pl-5">
                    <div class="flex items-center">
                      <p class="ml-2 text-sm leading-none text-gray-600">價錢</p>
                    </div>
                  </td>
                  <td class="pl-4">
                    <p class="ml-2 text-sm leading-none text-gray-600">訂單內容</p>
                  </td>
                  <td class="pl-4">
                    <p class="ml-2 text-sm leading-none text-gray-600">訂單狀態</p>
                  </td>
                </tr>
                <tr v-for="order in historyOrder" tabindex="0" class="h-16 rounded border border-gray-100 focus:outline-none">
                  <td>
                    <div class="ml-5">
                      <div
                        class="relative flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-sm bg-gray-200"
                      >
                        <input
                          placeholder="checkbox"
                          type="checkbox"
                          class="checkbox absolute h-full w-full cursor-pointer opacity-0 focus:opacity-100"
                          @click="test(order.customer_id)"
                        />
                        <div class="check-icon hidden rounded-sm bg-indigo-700 text-white">
                          <svg
                            class="icon icon-tabler icon-tabler-check"
                            xmlns="http://www.w3.org/2000/svg"
                            width="20"
                            height="20"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            fill="none"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                          >
                            <path stroke="none" d="M0 0h24v24H0z"></path>
                            <path d="M5 12l5 5l10 -10"></path>
                          </svg>
                        </div>
                      </div>
                    </div>
                  </td>
                  <td class="">
                    <div class="flex items-center pl-5">
                      <p class="mr-2 text-base font-medium leading-none text-gray-700">{{ order.order_time }}</p>
                    </div>
                  </td>
                  <td class="pl-24"></td>
                  <td class="pl-5"></td>
                  <td class="pl-5"></td>
                  <td class="pl-0">
                    <p class="ml-2 text-sm leading-none text-gray-600">{{ order.customer_id }}</p>
                  </td>
                  <td class="pl-5">
                    <p class="ml-2 text-sm leading-none text-gray-600">${{ order.price }}</p>
                  </td>
                  <td class="pl-4">
                    <button
                      class="rounded bg-gray-100 px-5 py-3 text-sm leading-none text-gray-600 hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-red-300 focus:ring-offset-2"
                    >
                      View
                    </button>
                  </td>
                  <td class="pl-4">
                    <button class="block py-3 text-sm focus:outline-none leading-none text-green-700 bg-green-100 rounded w-20"> done    </button>
                                
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia'
import restaurantService from '@/service/restaurantService'
import type { restaurant, meal, order } from '@/types/restaurant'
import { useUserStore } from '@/store/user'
import router from '@/router'

const userStore = useUserStore()
const { userInfo } = storeToRefs(userStore)
const historyOrder = ref<order[]>()

onMounted(async () => {
  historyOrder.value = await restaurantService.getHistoryOrder(userInfo.value.outh_token)
  console.log(historyOrder.value)

})

const test = (id: string) => {
  console.log(id)
}

</script>

