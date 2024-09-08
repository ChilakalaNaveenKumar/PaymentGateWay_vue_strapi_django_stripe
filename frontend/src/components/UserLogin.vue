<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input v-model="username" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import axiosInstance from '@/axiosInstance';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        error: null,
      };
    },
    methods: {
      async login() {
        try {
          // Send login request to Django backend
          await axiosInstance.post('/auth/login/', {
            username: this.username,
            password: this.password,
          });
          this.$router.push('/products'); // Navigate to the products page after successful login
        } catch (err) {
          this.error = 'Invalid login';
        }
      },
    },
  };
  </script>
  