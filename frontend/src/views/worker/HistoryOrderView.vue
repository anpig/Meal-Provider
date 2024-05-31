<template>
  <SuccessDialog v-if="showDialog" @close="close()" message=""></SuccessDialog>
  <div class="mx-auto bg-white px-5">
    <div class="flex flex-col-reverse lg:flex-row">
      <WorkerSidebar class="min-h-screen w-full shadow-lg lg:w-1/6"></WorkerSidebar>
      <div class="min-h-screen mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:w-5/6 lg:px-8 lg:pb-24">
        <div class="max-w-xl">
          <h1 class="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">Order history</h1>
          <!-- <p class="mt-2 text-sm text-gray-500">Check the status of recent orders, manage returns, and download invoices.</p> -->
        </div>

        <div class="mt-16">
          <div class="space-y-20">
            <div v-for="order in orders">
              <div
                class="rounded-lg bg-gray-100 px-4 py-6 sm:flex sm:items-center sm:justify-between sm:space-x-6 sm:px-6 lg:space-x-8"
                v-if="order.reviewed === true"
              >
                <dl
                  class="flex-auto space-y-6 divide-y divide-gray-200 text-sm text-gray-600 sm:grid sm:grid-cols-3 sm:gap-x-6 sm:space-y-0 sm:divide-y-0 lg:w-1/2 lg:flex-none lg:gap-x-8"
                >
                  <div class="flex justify-between sm:block">
                    <dt class="font-medium text-gray-900">Date placed</dt>
                    <dd class="sm:mt-1">
                      <time>{{ order.order_time }}</time>
                    </dd>
                  </div>
                  <div class="flex justify-between pt-6 font-medium text-gray-900 sm:block sm:pt-0">
                    <dt>Total amount</dt>
                    <dd class="sm:mt-1">${{ order.total_price }}</dd>
                  </div>
                </dl>
                <a
                  href="#"
                  class="mt-6 flex w-full items-center justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:mt-0 sm:w-auto"
                >
                  View Restaurant
                </a>
              </div>
              <div
                class="rounded-lg bg-gray-100 px-4 py-6 sm:flex sm:items-center sm:justify-between sm:space-x-6 sm:px-6 lg:space-x-8"
                v-else
              >
                <dl
                  class="flex-auto space-y-6 divide-y divide-gray-200 text-sm text-gray-600 sm:grid sm:grid-cols-3 sm:gap-x-6 sm:space-y-0 sm:divide-y-0 lg:w-1/2 lg:flex-none lg:gap-x-8"
                >
                  <div class="flex justify-between sm:block">
                    <dt class="font-medium text-gray-900">Date placed</dt>
                    <dd class="sm:mt-1">
                      <time>{{ order.order_time }}</time>
                    </dd>
                  </div>
                  <div class="flex justify-between pt-6 font-medium text-gray-900 sm:block sm:pt-0">
                    <dt>Total amount</dt>
                    <dd class="sm:mt-1">${{ order.total_price }}</dd>
                  </div>
                </dl>
                <button
                  class="mt-6 flex w-full items-center justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:mt-0 sm:w-auto"
                  @click="test()"
                >
                  Rate Order
                </button>
                <a
                  href="#"
                  class="mt-6 flex w-full items-center justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:mt-0 sm:w-auto"
                >
                  View Restaurant
                </a>
              </div>

              <table class="mt-4 w-full text-gray-500 sm:mt-6">
                <caption class="sr-only">
                  Products
                </caption>
                <thead class="sr-only text-left text-sm text-gray-500 sm:not-sr-only">
                  <tr>
                    <th scope="col" class="py-3 pr-8 font-normal sm:w-2/5 lg:w-1/3">Product</th>
                    <th scope="col" class="hidden w-1/5 py-3 pr-8 font-normal sm:table-cell">Number</th>
                    <th scope="col" class="hidden w-1/5 py-3 pr-8 font-normal sm:table-cell">Rating</th>
                    <th scope="col" class="w-0 py-3 pr-8 text-right font-normal">Price</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200 border-b border-gray-200 text-sm sm:border-t">
                  <tr v-for="dish in order.dishes">
                    <td class="py-6 pr-8">
                      <div class="flex items-center">
                        <!-- <img
                          src="https://source.unsplash.com/sc5sTPMrVfk/600x600"
                          alt="Detail of mechanical pencil tip with machined black steel shaft and chrome lead tip."
                          class="mr-6 h-16 w-16 rounded object-cover object-center"
                        /> -->
                        <div>
                          <div class="font-medium text-gray-900">{{ dish.dish_name }}</div>
                        </div>
                      </div>
                    </td>
                    <td class="py-6 pr-8 sm:table-cell">{{ dish.number }}</td>
                    <td class="py-6 pr-8 sm:table-cell">
                      <div class="flex items-center" v-if="order.reviewed === true">
                        <svg
                          class="me-1 h-4 w-4 text-yellow-300"
                          aria-hidden="true"
                          xmlns="http://www.w3.org/2000/svg"
                          fill="currentColor"
                          viewBox="0 0 22 20"
                        >
                          <path
                            d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"
                          />
                        </svg>
                        <p class="ms-2 text-sm font-bold text-gray-900">{{ dish.rating }}</p>
                      </div>
                    </td>
                    <td class="py-3 pr-8 text-right sm:table-cell">$ {{ dish.price }}</td>
                  </tr>

                  <!-- More products... -->
                </tbody>
              </table>
            </div>

            <!-- More orders... -->
          </div>
        </div>
        <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
          <table class="w-full text-sm text-left rtl:text-right">
              <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                  <tr>
                      <th scope="col" class="px-6 py-3">
                          Product name
                      </th>
                      <th scope="col" class="px-6 py-3">
                          <div class="flex items-center">
                              Color
                              <a href="#"><svg class="w-3 h-3 ms-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
          <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
        </svg></a>
                          </div>
                      </th>
                      <th scope="col" class="px-6 py-3">
                          <div class="flex items-center">
                              Category
                              <a href="#"><svg class="w-3 h-3 ms-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
          <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
        </svg></a>
                          </div>
                      </th>
                      <th scope="col" class="px-6 py-3">
                          <div class="flex items-center">
                              Price
                              <a href="#"><svg class="w-3 h-3 ms-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
          <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
        </svg></a>
                          </div>
                      </th>
                      <th scope="col" class="px-6 py-3">
                          <span class="sr-only">Edit</span>
                      </th>
                  </tr>
              </thead>
              <tbody>
                  <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                      <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                          Apple MacBook Pro 17"
                      </th>
                      <td class="px-6 py-4">
                          Silver
                      </td>
                      <td class="px-6 py-4">
                          Laptop
                      </td>
                      <td class="px-6 py-4">
                          $2999
                      </td>
                      <td class="px-6 py-4 text-right">
                          <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
                      </td>
                  </tr>
                  <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                      <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                          Microsoft Surface Pro
                      </th>
                      <td class="px-6 py-4">
                          White
                      </td>
                      <td class="px-6 py-4">
                          Laptop PC
                      </td>
                      <td class="px-6 py-4">
                          $1999
                      </td>
                      <td class="px-6 py-4 text-right">
                          <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
                      </td>
                  </tr>
                  <tr class="bg-white dark:bg-gray-800">
                      <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                          Magic Mouse 2
                      </th>
                      <td class="px-6 py-4">
                          Black
                      </td>
                      <td class="px-6 py-4">
                          Accessories
                      </td>
                      <td class="px-6 py-4">
                          $99
                      </td>
                      <td class="px-6 py-4 text-right">
                          <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
                      </td>
                  </tr>
              </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed, reactive, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import workerService from '@/service/workerService'
import { useUserStore } from '@/store/user'
import type { order } from '@/types/worker'
import SuccessDialog from '@/components/successDialog.vue'

const userStore = useUserStore()
const { userInfo } = storeToRefs(userStore)
const showDialog = ref(false)
const orders = ref<order[]>([])

onMounted(async () => {
  await getHistortOrder()
})

const getHistortOrder = async () => {
  const data = await workerService.getHistoryOrder(userInfo.value.outh_token)
  orders.value = data
}

const test = () => {
  showDialog.value = true
}

const close = () => {
  showDialog.value = false
}
</script>

<style></style>
