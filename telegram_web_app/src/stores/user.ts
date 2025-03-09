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

  // Действия
  const setTelegramUsername = (username: string) => {
    telegramUsername.value = username;
  };

  const setBirthDate = (date: string) => {
    birthDate.value = date;
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
    setTelegramUsername,
    setBirthDate,
    fetchTimeLeft,
  };
});