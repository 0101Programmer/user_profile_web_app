<template>
  <div class="p-4 gradient-bg">

    <h1 class="text-2xl mt-4">Введи свою дату рождения</h1>
    <br>
    <input
      type="date"
      v-model="birthDate"
      class="mt-2 p-2 border rounded"
    />
    <br><br>

    <!-- Отображение введенной даты -->
    <p class="mt-2 text-lg">
      Ты ввел(а): <span class="font-bold">{{ birthDate }}</span>
    </p>

    <button
      @click="nextPage"
      class="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
    >
      Продолжить
    </button>
  </div>
</template>

<script setup lang="ts">
import { useMainStore } from './stores';
import { ref } from 'vue';

const store = useMainStore();
const birthDate = ref(''); // Переменная для даты рождения
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #6a11cb, #2575fc); /* Градиент */
  min-height: 100vh; /* Чтобы фон занимал всю высоту экрана */
  color: white; /* Цвет текста для контраста */
}
</style>