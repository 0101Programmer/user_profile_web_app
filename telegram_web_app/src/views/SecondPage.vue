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
        <p class="font-bold">{{ telegram_username }}</p>
      </div>

      <!-- Дата рождения -->
      <div class="mb-4">
        <label class="block text-lg mb-2">До дня рождения осталось:</label>
        <p class="font-bold">{{ time_left }}</p>
      </div>

      <button
      @click="copyLink"
      class="mt-4 px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        Поделиться
      </button>

    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute(); // Получаем доступ к текущему маршруту
const time_left = route.query.time_left; // Получаем данные из query-параметров
const telegram_username = route.query.telegram_username;

const userFirstName = ref(''); // Имя
const userLastName = ref(''); // Фамилия
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #6a11cb, #2575fc); /* Градиент */
  color: white; /* Цвет текста для контраста */
}
</style>