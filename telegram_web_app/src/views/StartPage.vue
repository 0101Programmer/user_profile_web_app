<template>
  <div class="p-4 gradient-bg flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-3xl mb-6">Введи свою дату рождения</h1>
    <div class="date-input-container">
      <input
        type="date"
        v-model="birthDate"
        class="custom-date-input mt-4 p-4 text-xl border-2 border-gray-800 rounded-lg"
      />
    </div>

    <button
      @click="sendBirthDate"
      v-if="isDateSelected"
      class="mt-6 px-6 py-3 bg-blue-600 text-white text-xl rounded-lg disabled:bg-gray-400 disabled:cursor-not-allowed shadow-lg"
    >
      Продолжить
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '../stores/user';

const router = useRouter();
const userStore = useUserStore();

// Получаем username как props
const props = defineProps({
  telegram_username: {
    type: String,
    required: true,
  },
});

// Устанавливаем username в хранилище
userStore.setTelegramUsername(props.telegram_username);

const birthDate = ref('');

const isDateSelected = computed(() => birthDate.value !== '');

const sendBirthDate = async () => {
  try {
    // Устанавливаем дату рождения в хранилище
    userStore.setBirthDate(birthDate.value);

    // Запрашиваем время до дня рождения
    await userStore.fetchTimeLeft();

    // Переходим на следующую страницу
    await router.push({ path: '/second' });
  } catch (error) {
    console.error('Ошибка при отправке данных:', error);
  }
};
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #6a11cb, #2575fc);
  color: white;
}

.custom-date-input {
  font-size: 1.5rem;
  padding: 1rem;
  background-color: #f9f9f9;
  color: #333;
  border: 2px solid #555;
  border-radius: 12px;
  width: 100%;
  max-width: 300px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.custom-date-input:focus {
  outline: none;
  border-color: #2575fc;
  box-shadow: 0 0 8px rgba(37, 117, 252, 0.5);
}

.date-input-container {
  display: flex;
  justify-content: center;
  width: 100%;
}
</style>