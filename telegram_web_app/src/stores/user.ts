import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';

export const useUserStore = defineStore('user', () => {
  // Состояние
  const telegramUsername = ref('');
  const userFirstName = ref('');
  const userLastName = ref('');
  const birthDate = ref('');
  const timeLeft = ref('');
  const isShared = ref(false); // Состояние для проверки была ли нажата кнопка поделиться
  const shareLink = ref('');

  // Действия
  const setTelegramUsername = (username: string) => {
    telegramUsername.value = username;
  };

  const setBirthDate = (date: string) => {
    birthDate.value = date;
  };

  const setShared = (value: boolean) => {
    isShared.value = value;
  };

  const setShareLink = (link: string) => {
    shareLink.value = link; // Установка ссылки
  };

  const fetchTimeLeft = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/birthday_counter/${birthDate.value}`);
      timeLeft.value = response.data.until_birthday;
    } catch (error) {
      console.error('Ошибка при запросе времени до дня рождения:', error);
      throw error;
    }
  };

  return {
    telegramUsername,
    userFirstName,
    userLastName,
    birthDate,
    timeLeft,
    isShared,
    shareLink,
    setTelegramUsername,
    setBirthDate,
    fetchTimeLeft,
    setShared,
    setShareLink,
  };
});