<template>
  <div class="p-4 bg-gradient-to-br from-[#6a11cb] to-[#2575fc] text-white flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-3xl font-bold mb-6">Выбери свою дату рождения</h1>

    <!-- Календарь -->
    <VCalendar
      v-model="birthDate"
      :attributes="attrs"
      @dayclick="onDayClick"
      class="w-full max-w-[350px] p-4 bg-white/10 backdrop-blur-lg border border-gray-700 rounded-2xl shadow-lg transition-transform hover:scale-105"
    />

    <!-- Кнопка -->
    <button
      @click="sendBirthDate"
      v-if="isDateSelected"
      class="mt-6 px-6 py-3 font-bold text-white bg-gradient-to-r from-purple-500 to-indigo-600 rounded-full shadow-lg hover:scale-105 transition-transform duration-200 max-w-[350px]"
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

// Обработчик выбора даты
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