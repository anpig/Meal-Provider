<template>
  <el-form :model="form">
    <el-form-item label="商品">
      <el-select v-model="form.item" placeholder="請選擇你要加進去的商品">
        <el-option label="蛋塔" value="蛋塔" />
        <el-option label="炸雞" value="炸雞" />
      </el-select>
    </el-form-item>
    <el-form-item label="數量">
      <el-input-number v-model="form.number" :min="1" :max="10" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="addItemToChart">新增商品</el-button>
    </el-form-item>
  </el-form>

  <el-table :data="charts" style="width: 100%">
    <el-table-column label="商品名稱" prop="item" />
    <el-table-column label="商品數量">
      <el-input-number v-model="form.number" :min="1" :max="10" />
    </el-table-column>
    <el-table-column label="number" prop="number" />
    <el-table-column>
      <template #default="scope">
        <el-button size="small" @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
        <el-button size="small" type="danger" @click="removeItem(scope.$index)">Delete</el-button>
      </template>
    </el-table-column>
  </el-table>

  <br />
  <div class="flex-container">
    <el-button type="primary" @click="addItemToChart">查詢最佳組合</el-button>
  </div>
</template>

<style>
.flex-container {
  display: flex;
  justify-content: flex-end;
  margin-right: 2%;
}
</style>

<script lang="ts" setup>
import { reactive } from 'vue'
import { useCouponStore } from '@/store/coupon'
import { storeToRefs } from 'pinia'
const couponStore = useCouponStore()

const { charts } = storeToRefs(couponStore)

const form = reactive({
  item: '蛋塔',
  number: 1
})

const addItemToChart = () => {
  couponStore.addItem({
    item: form.item,
    number: form.number
  })
  form.number = 1
}

const handleEdit = (x: number, row: any) => {
  console.log(x, row)
}

const removeItem = (x: number) => {
  couponStore.removeItem(x)
}
const handleDelete = (x: number, row: any) => {
  console.log(x, row)
}
</script>
