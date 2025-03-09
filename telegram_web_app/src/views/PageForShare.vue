<template>
  <div class="p-4 bg-gradient-to-br from-[#6a11cb] to-[#2575fc] text-white flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-3xl font-bold mb-6">Данные пользователя</h1>

    <!-- Контейнер для данных -->
    <div class="w-full max-w-md bg-white/10 backdrop-blur-lg rounded-2xl p-6 shadow-lg">
      <!-- Имя -->
      <div class="mb-4">
        <label class="block text-lg mb-2 text-gray-300">Имя:</label>
        <p class="font-bold text-xl">{{ userData.first_name }}</p>
      </div>

      <!-- Фамилия -->
      <div class="mb-4">
        <label class="block text-lg mb-2 text-gray-300">Фамилия:</label>
        <p class="font-bold text-xl">{{ userData.last_name }}</p>
      </div>

      <!-- Юзернейм -->
      <div class="mb-4">
        <label class="block text-lg mb-2 text-gray-300">Юзернейм:</label>
        <p class="font-bold text-xl">{{ userData.telegram_username }}</p>
      </div>

      <!-- Дней до дня рождения -->
      <div class="mb-4">
        <label class="block text-lg mb-2 text-gray-300">До дня рождения осталось:</label>
        <p class="font-bold text-xl">{{ userData.time_left }}</p>
      </div>

      <!-- Кнопка для копирования ссылки -->
      <div class="mb-4">
        <button
          @click="copyToClipboard(`http://localhost:5175/share_page/${shareLink}`)"
          class="w-full px-6 py-3 font-bold text-white bg-gradient-to-r from-purple-500 to-indigo-600 rounded-full shadow-lg hover:scale-105 transition-transform duration-200"
        >
          Поделиться
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const router = useRouter();
const shareLink = route.params.share_link; // Получаем share_link из параметров маршрута

const userData = ref({
  first_name: '',
  last_name: '',
  telegram_username: '',
  time_left: '',
});

// Функция для получения данных пользователя
const fetchUserData = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/get_user_data/${shareLink}`);

    // Проверяем, найден ли пользователь
    if (response.data.user === false) {
      // Перенаправляем на страницу "Пользователь не найден"
      await router.push('/user_not_found');
    } else {
      // Сохраняем данные пользователя
      userData.value = response.data;
    }
  } catch (error) {
    console.error('Ошибка при получении данных пользователя:', error);
  }
};

// Метод для копирования ссылки
const copyToClipboard = async (link: string) => {
  try {
    await navigator.clipboard.writeText(link);
    alert('Ссылка скопирована в буфер обмена!');
  } catch (error) {
    console.error('Ошибка при копировании ссылки:', error);
    alert('Не удалось скопировать ссылку. Попробуйте еще раз.');
  }
};

// Выполняем запрос при монтировании компонента
onMounted(() => {
  fetchUserData();
});
</script>