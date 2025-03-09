<template>
  <div class="p-4 gradient-bg flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-2xl mb-4">Введи свою дату рождения</h1>
    <input
      type="date"
      v-model="birthDate"
      class="mt-2 p-2 border rounded"
    />

    <button
      @click="sendBirthDate"
      :disabled="!isDateSelected"
      class="mt-4 px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
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
</style>