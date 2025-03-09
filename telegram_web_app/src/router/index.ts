import { createRouter, createWebHistory } from 'vue-router';
import StartPage from '../views/StartPage.vue'; // Стартовая страница
import SecondPage from '../views/SecondPage.vue'; // Вторая страница
import PageForShare from '../views/PageForShare.vue'; // Страница, для того чтобы ей поделиться
import UserNotFondPage from '../views/UserNotFondPage.vue'; // Страница, для обработки ошибки, когда пользователь не найден


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
  {
    path: '/share_page/:share_link',
    component: PageForShare,
    props: true,
  },
  {
    path: '/user_not_found/',
    component: UserNotFondPage,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;