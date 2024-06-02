<template>
  <div class="mx-auto bg-white">
    <div class="flex flex-col-reverse lg:flex-row gap-4">
      <AdminSidebar class="min-h-screen w-full shadow-lg lg:w-1/6"></AdminSidebar>

      <div class=" lg:w-5/6">
        <div class="font-bold text-4xl px-5 py-6">{{ restaurantInfo?.restaurant }}</div>
        <div class="font-bold text-lg mb-4 px-5">
          營業時間: {{ restaurantInfo?.open_time }} - {{ restaurantInfo?.close_time }}
        </div>
        <div class="font-bold text-lg mb-4 px-5">電話: {{ restaurantInfo?.phone }}</div>
        <div class="grid grid-cols-1 gap-10 sm:grid-cols-2 md:grid-cols-4">
            <div
              style="cursor: pointer"
              class="flex h-32 flex-col justify-between rounded-md border bg-white px-3 py-3"
              v-for="meal in restaurantMeals"
            >
              <div>
                <div class="font-bold text-gray-800">{{ meal.name }}</div>
              </div>
              <div class="flex flex-row items-center justify-between">
                <span class="self-end text-lg font-bold text-yellow-500">${{ meal.price }}</span>
                <img :src="'/api' + meal.picture" class="h-14 w-14 rounded-md object-cover" alt="" />
              </div>
            </div>
          </div> 
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useRoute } from 'vue-router'
import { ref, computed, reactive, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import workerService from '@/service/workerService'
import userService from '@/service/userService'
import { useUserStore } from '@/store/user'
import type { restaurant, meal } from '@/types/worker'
import router from '@/router'

const userStore = useUserStore()
const { userInfo } = storeToRefs(userStore)
const route = useRoute()
const restaurantId = route.params.id
const restaurantInfo = ref<restaurant>()
const restaurantMeals = ref<meal[]>([])

onMounted(async () => {
  const OuthResult = await userService.userCheckOuth()
  if (OuthResult === false) {
    alert('請重新登入')
    router.push('/')
  }
  await getRestaurant()
})

const getRestaurant = async () => {
  restaurantInfo.value = await workerService.getRestaurant(userInfo.value.outh_token, restaurantId[0])
  restaurantMeals.value = restaurantInfo.value.meals
}
</script>
