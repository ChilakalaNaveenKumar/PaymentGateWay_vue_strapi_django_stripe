<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="register">
        <input v-model="username" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button type="submit">Register</button>
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
      async register() {
        try {
          // Fetch CSRF token from Django
          // const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrftoken')).split('=')[1];

          await axiosInstance.post('/auth/register/', {
            username: this.username,
            password: this.password,
          });
          this.$router.push('/login');
        } catch (err) {
          console.log(err)
          // this.error = 'Registration failed: ' + JSON.stringify(err.response.data);
        }
      },
    },
  };
  </script>
  