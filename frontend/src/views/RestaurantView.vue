<template>
  <div>
    <h1>{{ restaurant.name }}</h1>
    <p>{{ restaurant.description }}</p>
    <ul>
      <li v-for="dish in restaurant.menu" :key="dish.id">{{ dish.name }} - {{ dish.price }}</li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const restaurant = ref({
  name: 'My Restaurant',
  description: 'Welcome to our restaurant!',
  menu: [
    { id: 1, name: 'Pizza', price: 10 },
    { id: 2, name: 'Burger', price: 8 },
    { id: 3, name: 'Salad', price: 6 }
  ]
})
</script>

<style scoped>
h1 {
  color: #333;
}

p {
  color: #777;
}

ul {
  list-style-type: none;
}

li {
  margin-bottom: 10px;
}
</style>
