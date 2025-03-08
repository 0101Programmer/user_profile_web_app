import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router'; // Импортируем роутер


const app = createApp(App);
app.use(createPinia());
app.use(router); // Используем роутер
app.mount('#app');
