import { createRouter, createWebHistory } from 'vue-router';
import StartPage from '../views/StartPage.vue'; // Стартовая страница
import SecondPage from '../views/SecondPage.vue'; // Вторая страница

const routes = [
  {
    path: '/web_page_for/:telegram_username',
    component: StartPage,
    props: true,
  },
  {
    path: '/second',
    component: SecondPage,
    props: true, // Разрешаем передачу параметров через props
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;