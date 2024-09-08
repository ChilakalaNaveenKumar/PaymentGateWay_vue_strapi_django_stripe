<template>
    <div>
      <h2>Forgot Password</h2>
      <form @submit.prevent="recoverPassword">
        <input v-model="email" placeholder="Email" type="email" />
        <button type="submit">Submit</button>
      </form>
      <p v-if="message">{{ message }}</p>
      <p v-if="error">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        email: '',
        message: null,
        error: null,
      };
    },
    methods: {
      async recoverPassword() {
        try {
          await axios.post('http://localhost:8000/auth/forgot-password/', { email: this.email });
          this.message = 'Password reset instructions sent!';
        } catch (err) {
          this.error = 'Error sending instructions';
        }
      },
    },
  };
  </script>
  