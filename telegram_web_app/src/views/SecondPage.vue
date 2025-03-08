<template>
  <div class="p-4 gradient-bg flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-2xl mb-4">Пользовательские данные:</h1>

    <!-- Контейнер для формы -->
    <div class="w-full max-w-md">
      <!-- Поле для имени -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Имя:</label>
        <input
          type="text"
          v-model="userFirstName"
          class="w-full p-2 border rounded"
        />
      </div>

      <!-- Поле для фамилии -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Фамилия:</label>
        <input
          type="text"
          v-model="userLastName"
          class="w-full p-2 border rounded"
        />
      </div>

      <!-- Юзернейм -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Юзернейм:</label>
        <input
          type="text"
          v-model="username"
          class="w-full p-2 border rounded"
        />
      </div>

      <!-- Дата рождения -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Дата рождения:</label>
        <p class="font-bold">{{ date }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute(); // Получаем доступ к текущему маршруту
const date = route.query.date; // Получаем дату из query-параметров

const userFirstName = ref(''); // Имя
const userLastName = ref(''); // Фамилия
const username = ref(''); // Юзернейм
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #6a11cb, #2575fc); /* Градиент */
  color: white; /* Цвет текста для контраста */
}
</style>