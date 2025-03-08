<template>
  <div class="p-4 gradient-bg flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-2xl mb-4">Спасибо за ввод даты!</h1>
    <p class="mt-2 text-lg">
      Ты ввел(а): <span class="font-bold">{{ date }}</span>
    </p>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'; // Импортируем useRoute

const route = useRoute(); // Получаем доступ к текущему маршруту
const date = route.query.date; // Получаем дату из query-параметров
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #6a11cb, #2575fc); /* Градиент */
  color: white; /* Цвет текста для контраста */
}
</style>