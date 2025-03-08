<template>
  <div class="p-4 gradient-bg flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-2xl mb-4">Введи свою дату рождения</h1>
    <input
      type="date"
      v-model="birthDate"
      class="mt-2 p-2 border rounded"
    />

    <button
      @click="secondPage"
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

const router = useRouter();

// Получаем username как props
const props = defineProps({
  telegram_username: {
    type: String,
    required: true,
  },
});

const birthDate = ref('');

const isDateSelected = computed(() => birthDate.value !== '');

const secondPage = () => {
  router.push({
    path: '/second',
    query: { birth_date: birthDate.value,
    telegram_username: props.telegram_username,},
  });
};
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #6a11cb, #2575fc);
  color: white;
}
</style>