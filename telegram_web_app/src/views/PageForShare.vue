<template>
  <div class="p-4 gradient-bg flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-2xl mb-4">Данные пользователя:</h1>

    <div class="w-full max-w-md">
      <!-- Имя -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Имя:</label>
        <p class="font-bold">{{ userData.first_name }}</p>
      </div>

      <!-- Фамилия -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Фамилия:</label>
        <p class="font-bold">{{ userData.last_name }}</p>
      </div>

      <!-- Юзернейм -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Юзернейм:</label>
        <p class="font-bold">{{ userData.telegram_username }}</p>
      </div>

      <!-- Дней до дня рождения -->
      <div class="mb-4">
        <label class="block text-lg mb-2">До дня рождения осталось:</label>
        <p class="font-bold">{{ userData.time_left }}</p>
      </div>

      <!-- Ссылка, чтобы поделиться с кем-то ещё -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Поделиться:</label>
        <a
          :href="`http://localhost:5175/share_page/${shareLink}`"
          @click.prevent="copyToClipboard(`http://localhost:5175/share_page/${shareLink}`)"
          class="font-bold block text-blue-300 hover:text-blue-100 hover:underline cursor-pointer transition-colors duration-200"
        >
          http://localhost:5175/share_page/{{ shareLink }}
        </a>
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

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #6a11cb, #2575fc);
  color: white;
}
</style>