<template>
  <div class="mx-auto min-h-screen max-w-screen-xl bg-white p-5 sm:p-10 md:p-16">
    <div class="flex flex-col-reverse gap-4 lg:flex-row">
      <WorkerSidebar class="w-full shadow-lg lg:w-1/6"></WorkerSidebar>

      <div class="grid grid-cols-1 gap-10 sm:grid-cols-2 md:grid-cols-4 lg:w-5/6">
        <div class="overflow-hidden rounded shadow-lg" v-for="restaurant in restaurants">
          <a :href="restaurant.url">
            <div class="relative">
              <img
                class="aspect-[3/2] w-full"
                :src="'/api' + restaurant.picture"
                alt="Sunset in the mountains"
              />
            </div>
            <div class="px-6 py-4">
              <p class="inline-block text-lg font-semibold transition duration-500 ease-in-out hover:text-indigo-600">
                {{ restaurant.restaurant }}
              </p>
              <div class="flex items-center">
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
                <p class="ms-2 text-sm font-bold text-gray-900">{{ restaurant.rating }}</p>
              </div>
            </div>
          </a>
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
import type { restaurant } from '@/types/worker'

const userStore = useUserStore()
const { userInfo } = storeToRefs(userStore)

const restaurants = ref<restaurant[]>([])

onMounted(async () => {
  await getRestaurantList()
  for (let i = 0; i < restaurants.value.length; i++) {
    restaurants.value[i].url = '/worker/restaurant/' + restaurants.value[i].id
  }
})

const getRestaurantList = async () => {
  const data = await workerService.getRestaurantList(userInfo.value.outh_token)
  restaurants.value = data
}
</script>

<style></style>
