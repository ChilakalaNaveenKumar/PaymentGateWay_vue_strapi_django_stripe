<template>
    <div>
      <h2>Products</h2>
      <ul>
        <li v-for="product in products" :key="product.id">
          {{ product.name }} - {{ product.price }} USD
          <button @click="goToPayment(product.id)">Buy Now</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
 import axiosInstance from '@/axiosInstance';
  
  export default {
    data() {
      return {
        products: [],
      };
    },
    async created() {
      // Axios will automatically include the cookie in this request
      try {
        // Fetch products with cookies automatically sent
        const response = await axiosInstance.get('/api/products/');
        this.products = response.data;
      } catch (error) {
        console.log('Error fetching products:', error);
      }
    },
    methods: {
      goToPayment(id) {
        this.$router.push(`/payment/${id}`);
      },
    },
  };
  </script>
  