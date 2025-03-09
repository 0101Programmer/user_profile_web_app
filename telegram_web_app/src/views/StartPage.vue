<template>
  <div class="p-4 gradient-bg flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-3xl mb-6 text-white">Выбери свою дату рождения</h1>

    <!-- Календарь -->
    <VCalendar
      v-model="birthDate"
      :attributes="attrs"
      @dayclick="onDayClick"
      class="custom-calendar mt-4 p-4 rounded-lg w-full max-w-[350px] shadow-lg transition-transform hover:scale-105"
    />

    <!-- Кнопка -->
    <button
      @click="sendBirthDate"
      v-if="isDateSelected"
      class="mt-6 px-6 py-3 bg-gradient-to-r from-purple-500 to-indigo-600 text-white text-xl font-bold rounded-full shadow-lg hover:scale-105 transition-transform"
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

// Дата рождения
const birthDate = ref<Date | null>(null);

// Проверка, выбрана ли дата
const isDateSelected = computed(() => !!birthDate.value);

const onDayClick = (day: any) => {
  birthDate.value = day.date; // Явно обновляем значение birthDate
};

// Настройки для выделения текущей даты
const attrs = ref([
  {
    key: 'today',
    highlight: {
      color: 'purple', // Цвет выделения
      fillMode: 'solid', // Заливка
    },
    dates: new Date(),
  },
]);

// Отправка даты рождения
const sendBirthDate = async () => {
  try {
    if (!birthDate.value) return;

    const formattedDate = birthDate.value.toISOString().split('T')[0];
    userStore.setBirthDate(formattedDate);
    await userStore.fetchTimeLeft();
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

.custom-calendar {
  background: rgba(255, 255, 255, 0.1); /* Полупрозрачный фон */
  backdrop-filter: blur(10px); /* Размытие */
  border: 2px solid rgba(255, 255, 255, 0.2); /* Светлая граница */
  border-radius: 16px; /* Скругленные углы */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); /* Тень */
  transition: transform 0.3s ease; /* Анимация увеличения */
}

.custom-calendar:hover {
  transform: scale(1.05); /* Эффект увеличения при наведении */
}
</style>