import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/components/UserLogin.vue';
import Register from '@/components/UserRegister.vue';
import ForgotPassword from '@/components/ForgotPassword.vue';
import Products from '@/components/ProductList.vue';
import Payment from '@/components/ProductPayment.vue';

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/forgot-password', component: ForgotPassword },
  { path: '/products', component: Products },
  { path: '/payment/:id', component: Payment },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
