<template>
  <router-view></router-view>
  <div class="p-4 gradient-bg flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-2xl mb-4">Введи свою дату рождения</h1>
    <input
      type="date"
      v-model="birthDate"
      class="mt-2 p-2 border rounded"
    />

    <button
      @click="secondPage"
      :disabled="!isDateSelected"
      class="mt-4 px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
    >
      Продолжить
    </button>
  </div>
</template>

<script setup lang="ts">
import { useMainStore } from './stores';
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router'; // Импортируем useRouter

const store = useMainStore();
const birthDate = ref(''); // Переменная для даты рождения
const router = useRouter(); // Получаем доступ к роутеру



// Вычисляемое свойство для проверки, выбрана ли дата
const isDateSelected = computed(() => birthDate.value !== '');

// Функция для перехода на следующую страницу
const secondPage = () => {
  console.log('Переход на страницу /second');
  // Переходим на страницу /second и передаём дату как параметр
  router.push({
    path: '/second',
    query: { date: birthDate.value }, // Передаём дату в query-параметрах
  });
};
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #6a11cb, #2575fc); /* Градиент */
  color: white; /* Цвет текста для контраста */
}
</style>