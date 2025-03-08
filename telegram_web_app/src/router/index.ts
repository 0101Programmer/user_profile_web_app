import { createRouter, createWebHistory } from 'vue-router';
import App from '../App.vue'; // Корневой компонент
import SecondPage from '../views/SecondPage.vue'; // Вторая страница

const routes = [
  {
    path: '/',
    component: App,
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