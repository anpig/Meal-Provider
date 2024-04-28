<template>
  <header>
    <el-menu mode="horizontal" text-color="#000" active-text-color="#000" router justify="space-center">
      <el-menu-item index="/">所有優惠卷</el-menu-item>
      <el-menu-item index="/search">查詢組合</el-menu-item>
    </el-menu>
  </header>
  <br />
  <RouterView />
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>
