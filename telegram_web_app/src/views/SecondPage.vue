<template>
  <div class="p-4 gradient-bg flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-2xl mb-4">Пользовательские данные:</h1>

    <!-- Контейнер для формы -->
    <div class="w-full max-w-md">

      <!-- Поле для имени, которое блокируется, если нажата кнопка "поделиться" -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Имя:</label>
        <input
          type="text"
          v-model="userStore.userFirstName"
          :disabled="userStore.isShared"
          class="w-full p-2 border rounded"
        />
      </div>

      <!-- Поле для фамилии, которое блокируется, если нажата кнопка "поделиться" -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Фамилия:</label>
        <input
          type="text"
          v-model="userStore.userLastName"
          :disabled="userStore.isShared"
          class="w-full p-2 border rounded"
        />
      </div>

      <!-- Юзернейм -->
      <div class="mb-4">
        <label class="block text-lg mb-2">Юзернейм:</label>
        <p class="font-bold">{{ userStore.telegramUsername }}</p>
      </div>

      <!-- Дата рождения -->
      <div class="mb-4">
        <label class="block text-lg mb-2">До дня рождения осталось:</label>
        <p class="font-bold">{{ userStore.timeLeft }}</p>
      </div>

      <!-- Кнопка "Поделиться" или ссылка на то, чтобы поделиться -->
      <div v-if="!userStore.isShared">
        <button
          @click="copyLink"
          v-if="fullName"
          class="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
        >
          Поделиться
        </button>
      </div>
      <div v-else>
        <a
            :href="userStore.shareLink"
            @click.prevent="copyToClipboard(userStore.shareLink)"
            class="mt-4 font-bold block text-blue-300 hover:text-blue-100 hover:underline cursor-pointer transition-colors duration-200"
        >
          {{ userStore.shareLink }}
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useUserStore } from '../stores/user';
import {computed} from "vue";
import axios from 'axios';

const userStore = useUserStore();

const fullName = computed(() => {
  if (userStore.userFirstName && userStore.userLastName) {
    return `${userStore.userFirstName} ${userStore.userLastName}`;
  }
  return '';
});

const copyLink = async () => {
  try {
    const userData = {
      first_name: userStore.userFirstName,
      last_name: userStore.userLastName,
      telegram_username: userStore.telegramUsername,
      birthdate: userStore.birthDate,
      time_left: userStore.timeLeft,
    };

    // Отправляем данные на сервер
    const response = await axios.post('http://127.0.0.1:8000/save_user_data/', userData);

    // Формируем полную ссылку
    const fullLink = `http://localhost:5175/share_page/${response.data.share_link}`;

    // Устанавливаем ссылку в хранилище
    userStore.setShareLink(fullLink);

    // Устанавливаем флаг isShared в true
    userStore.setShared(true);

    console.error('Данные успешно сохранены');
  } catch (error) {
    console.error('Ошибка при сохранении данных:', error);
  }
};

// Метод для копирования ссылки
const copyToClipboard = async (link: string) => {
  try {
    await navigator.clipboard.writeText(link); // Копируем текст в буфер обмена
    alert('Ссылка скопирована в буфер обмена!'); // Оповещаем пользователя
  } catch (error) {
    console.error('Ошибка при копировании ссылки:', error);
    alert('Не удалось скопировать ссылку. Попробуйте еще раз.');
  }
};
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #6a11cb, #2575fc);
  color: white;
}
</style>