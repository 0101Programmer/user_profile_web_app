<template>
  <div class="p-4 bg-gradient-to-br from-[#6a11cb] to-[#2575fc] text-white flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-3xl font-bold mb-6">Пользовательские данные</h1>

    <!-- Контейнер для формы -->
    <div class="w-full max-w-md bg-white/10 backdrop-blur-lg rounded-2xl p-6 shadow-lg">
      <!-- Поле для имени -->
      <div class="mb-4">
        <label class="block text-lg mb-2 text-gray-300">Имя:</label>
        <input
          type="text"
          v-model="userStore.userFirstName"
          :disabled="userStore.isShared"
          class="w-full p-3 border border-gray-700 rounded-lg bg-transparent text-white placeholder:text-gray-400 focus:outline-none focus:border-purple-500 transition-colors duration-200"
          placeholder="Введите имя"
        />
      </div>

      <!-- Поле для фамилии -->
      <div class="mb-4">
        <label class="block text-lg mb-2 text-gray-300">Фамилия:</label>
        <input
          type="text"
          v-model="userStore.userLastName"
          :disabled="userStore.isShared"
          class="w-full p-3 border border-gray-700 rounded-lg bg-transparent text-white placeholder:text-gray-400 focus:outline-none focus:border-purple-500 transition-colors duration-200"
          placeholder="Введите фамилию"
        />
      </div>

      <!-- Юзернейм -->
      <div class="mb-4">
        <label class="block text-lg mb-2 text-gray-300">Юзернейм:</label>
        <p class="font-bold text-xl">{{ userStore.telegramUsername }}</p>
      </div>

      <!-- Дата рождения -->
      <div class="mb-4">
        <label class="block text-lg mb-2 text-gray-300">До дня рождения осталось:</label>
        <p class="font-bold text-xl">{{ userStore.timeLeft }}</p>
      </div>

      <!-- Кнопка "Поделиться" или ссылка на то, чтобы поделиться -->
      <div v-if="!userStore.isShared" class="mb-4">
        <button
          @click="copyLink"
          v-if="fullName"
          class="w-full px-6 py-3 font-bold text-white bg-gradient-to-r from-purple-500 to-indigo-600 rounded-full hover:scale-105 transition-transform duration-200 shadow-lg"
        >
          Поделиться
        </button>
      </div>
      <div v-else class="mb-4">
        <button
          @click="copyToClipboard(userStore.shareLink)"
          class="w-full px-6 py-3 font-bold text-white bg-gradient-to-r from-purple-500 to-indigo-600 rounded-full hover:scale-105 transition-transform duration-200 shadow-lg"
        >
          Скопировать ссылку
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useUserStore } from '../stores/user';
import { computed } from 'vue';
import axios from 'axios';

const userStore = useUserStore();

// Вычисляем заполнены ли поля имя и фамилия для отображения кнопки
const fullName = computed(() => {
  if (userStore.userFirstName && userStore.userLastName) {
    return `${userStore.userFirstName} ${userStore.userLastName}`;
  }
  return '';
});

// Метод для отправки данных на сервер
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

    // Устанавливаем флаг isShared в true для того, чтобы нельзя было поменять поле имя и фамилия
    userStore.setShared(true);

    console.log('Данные успешно сохранены');
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